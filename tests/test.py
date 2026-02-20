import ast
from textwrap import dedent

from flake8_qiskit_migration.plugin import Plugin


def _results(code: str):
    code = dedent(code)
    tree = ast.parse(code)
    plugin = Plugin(tree)
    return {f"{line}:{col} {msg}" for line, col, msg, _ in plugin.run()}


def test_trivial_case():
    assert _results("") == set()


def test_simple_import_path():
    code = """
    from qiskit import QuantumCircuit
    import qiskit.extensions
    import qiskit.extensions.item  # should raise error even though `.item` doesn't exist as whole path is deprecated
    import qiskit.quantum_info.synthesis.OneQubitEulerDecomposer
    import numpy
    """
    assert _results(code) == {
        "3:0 QKT100: qiskit.extensions has been removed; most objects have been moved to `qiskit.circuit.library` (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features)",
        "4:0 QKT100: qiskit.extensions.item has been removed; most objects have been moved to `qiskit.circuit.library` (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features)",
        "5:0 QKT100: qiskit.quantum_info.synthesis.OneQubitEulerDecomposer has moved to `qiskit.synthesis.one_qubit.OneQubitEulerDecomposer`",
    }


def test_simple_from_import_path():
    code = """
    from qiskit.quantum_info.synthesis import OneQubitEulerDecomposer
    from qiskit.quantum_info.synthesis import XXDecomposer as xxd
    from qiskit.quantum_info.synthesis import NonDeprecatedClass
    from qiskit.quantum_info.synthesis import OtherNonDeprecatedClass as XXDecomposer
    """
    assert _results(code) == {
        "2:0 QKT100: qiskit.quantum_info.synthesis.OneQubitEulerDecomposer has moved to `qiskit.synthesis.one_qubit.OneQubitEulerDecomposer`",
        "3:0 QKT100: qiskit.quantum_info.synthesis.XXDecomposer has moved to `qiskit.synthesis.two_qubits.XXDecomposer`",
    }


def test_module_attribute_later_in_script():
    code = """
    import qiskit.quantum_info.synthesis
    xxd = qiskit.quantum_info.synthesis.XXDecomposer()
    qiskit.quantum_info.synthesis.OneQubitEulerDecomposer().run()
    allowed = qiskit.quantum_info.synthesis.AllowedPath
    """
    assert _results(code) == {
        "3:6 QKT100: qiskit.quantum_info.synthesis.XXDecomposer has moved to `qiskit.synthesis.two_qubits.XXDecomposer`",
        "4:0 QKT100: qiskit.quantum_info.synthesis.OneQubitEulerDecomposer has moved to `qiskit.synthesis.one_qubit.OneQubitEulerDecomposer`",
    }


def test_module_attribute_later_in_script_with_alias():
    code = """
    import qiskit as qk
    qk.extensions.thing()
    """
    assert _results(code) == {
        "3:0 QKT100: qiskit.extensions.thing has been removed; most objects have been moved to `qiskit.circuit.library` (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features)",
    }


def test_alias_scope():
    code = """
    import safe_module as qk

    def my_function():
        import qiskit as qk
        return qk.extensions.thing()  # deprecated

    print(qk.extensions.thing())  # safe import
    """
    assert _results(code) == {
        "6:11 QKT100: qiskit.extensions.thing has been removed; most objects have been moved to `qiskit.circuit.library` (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features)",
    }

    code = """
    import qiskit as qk

    def my_function():
        import safe_module as qk
        return qk.extensions.thing()  # safe

    print(qk.extensions.thing())  # deprecated
    """
    assert _results(code) == {
        "8:6 QKT100: qiskit.extensions.thing has been removed; most objects have been moved to `qiskit.circuit.library` (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features)",
    }

def test_exceptions():
    code = """
    from qiskit.fake_provider.utils import json_decoder
    """
    assert _results(code) == set()

def test_basicaer():
    code = """
    from qiskit import BasicAer
    """
    assert _results(code) == {
        "2:0 QKT100: qiskit.BasicAer has been removed; either install separate `qiskit-aer` package and replace import with `qiskit_aer.Aer`, or follow https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#providers.basicaer"
    }

def test_providers():
    code = """
    from qiskit.providers.fake_provider import FakeCairo
    from qiskit.providers.fake_provider import GenericBackendV2
    from qiskit.providers.fake_provider import FakeBackend
    """
    assert _results(code) == {
        "2:0 QKT100: qiskit.providers.fake_provider.FakeCairo has moved; install separate `qiskit-ibm-runtime` package and replace `qiskit.providers.fake_provider` with `qiskit_ibm_runtime.fake_provider`",
        "2:0 QKT200: qiskit.providers.fake_provider.FakeCairo has been removed in Qiskit 2.0; use `GenericBackendV2` or `qiskit_ibm_runtime.fake_provider`",
        "4:0 QKT200: qiskit.providers.fake_provider.FakeBackend has been removed in Qiskit 2.0; use `GenericBackendV2` or `qiskit_ibm_runtime.fake_provider`",
    }

def test_utils():
    code = """
    from qiskit.utils import valid_import
    from qiskit.utils import QuantumInstance, entangler_map
    """
    assert _results(code) == {
        "3:0 QKT100: qiskit.utils.entangler_map has been removed with no replacement",
        "3:0 QKT100: qiskit.utils.QuantumInstance has been removed; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-quantum-instance"
    }


# ---- QKT200 tests (Qiskit 2.0 removals) ----

def test_pulse_removal():
    code = """
    import qiskit.pulse
    from qiskit.pulse import ScheduleBlock
    from qiskit.pulse.library import Gaussian
    """
    results = _results(code)
    assert all("QKT200" in r for r in results)
    assert len(results) == 3


def test_qobj_removal():
    code = """
    from qiskit.qobj import QasmQobj
    import qiskit.qobj
    """
    results = _results(code)
    assert all("QKT200" in r for r in results)
    assert len(results) == 2


def test_classicalfunction_removal():
    code = """
    from qiskit.circuit.classicalfunction import ClassicalFunction
    from qiskit.circuit.classicalfunction import BooleanExpression
    """
    results = _results(code)
    assert all("QKT200" in r for r in results)
    assert len(results) == 2


def test_backendv1_removal():
    code = """
    from qiskit.providers import BackendV1
    from qiskit.providers import BackendV2Converter
    """
    results = _results(code)
    assert all("QKT200" in r for r in results)
    assert len(results) == 2


def test_provider_models_removal():
    code = """
    from qiskit.providers.models import BackendConfiguration
    from qiskit.providers.models import BackendProperties
    """
    results = _results(code)
    assert all("QKT200" in r for r in results)
    assert len(results) == 2


def test_primitive_v1_removal():
    code = """
    from qiskit.primitives import Estimator
    from qiskit.primitives import Sampler
    from qiskit.primitives import BackendEstimator
    from qiskit.primitives import BackendSampler
    from qiskit.primitives import StatevectorEstimator
    from qiskit.primitives import StatevectorSampler
    """
    results = _results(code)
    # StatevectorEstimator and StatevectorSampler are exceptions (valid V2 classes)
    qkt200_results = {r for r in results if "QKT200" in r}
    assert len(qkt200_results) == 4


def test_transpiler_passes_v2():
    code = """
    from qiskit.transpiler.passes import ASAPSchedule
    from qiskit.transpiler.passes import CXCancellation
    from qiskit.transpiler.passes import StochasticSwap
    from qiskit.transpiler.passes import PulseGates
    """
    results = _results(code)
    qkt200_results = {r for r in results if "QKT200" in r}
    assert len(qkt200_results) == 4


def test_assembler_removal():
    code = """
    from qiskit.assembler import assemble_circuits
    from qiskit.compiler import assemble
    """
    results = _results(code)
    qkt200_results = {r for r in results if "QKT200" in r}
    assert len(qkt200_results) == 2


def test_scheduler_removal():
    code = """
    from qiskit.scheduler import schedule_circuit
    """
    results = _results(code)
    assert any("QKT200" in r for r in results)


def test_result_mitigation_removal():
    code = """
    from qiskit.result.mitigation import LocalReadoutMitigator
    """
    results = _results(code)
    assert any("QKT200" in r for r in results)


def test_visualization_v2():
    code = """
    from qiskit.visualization import pulse_drawer
    from qiskit.visualization import visualize_transition
    """
    results = _results(code)
    qkt200_results = {r for r in results if "QKT200" in r}
    assert len(qkt200_results) == 2


def test_fake_backend_v1_removal():
    code = """
    from qiskit.providers.fake_provider import FakeBackend
    from qiskit.providers.fake_provider import Fake1Q
    from qiskit.providers.fake_provider import GenericBackendV2
    """
    results = _results(code)
    # FakeBackend and Fake1Q should trigger QKT200
    # GenericBackendV2 is an exception (still valid)
    qkt200_results = {r for r in results if "QKT200" in r}
    assert len(qkt200_results) == 2


def test_both_codes_pulse():
    """qiskit.pulse paths that were deprecated in 1.0 AND removed in 2.0
    should produce both QKT100 and QKT200 messages."""
    code = """
    from qiskit.pulse.library.parametric_pulses import Gaussian
    """
    results = _results(code)
    assert any("QKT100" in r for r in results)
    assert any("QKT200" in r for r in results)


def test_v2_only_no_v1():
    """Paths removed in 2.0 but NOT deprecated in 1.0 should only produce QKT200."""
    code = """
    from qiskit.providers import BackendV1
    """
    results = _results(code)
    assert any("QKT200" in r for r in results)
    assert not any("QKT100" in r for r in results)


def test_v2_exceptions():
    """V2 exceptions should not trigger QKT200."""
    code = """
    from qiskit.primitives import StatevectorEstimator
    from qiskit.primitives import BaseEstimatorV2
    from qiskit.providers.fake_provider import GenericBackendV2
    """
    results = _results(code)
    qkt200_results = {r for r in results if "QKT200" in r}
    assert len(qkt200_results) == 0


def test_compiler_sequence_schedule_removal():
    code = """
    from qiskit.compiler import sequence
    from qiskit.compiler import schedule
    """
    results = _results(code)
    qkt200_results = {r for r in results if "QKT200" in r}
    assert len(qkt200_results) == 2
    assert all("Pulse removal" in r for r in qkt200_results)


def test_rzx_templates_removal():
    code = """
    from qiskit.transpiler.passes import rzx_templates
    """
    results = _results(code)
    assert any("QKT200" in r and "Pulse removal" in r for r in results)


def test_no_false_positives():
    """Valid Qiskit 2.0 imports should not trigger any warnings."""
    code = """
    from qiskit.circuit import QuantumCircuit
    from qiskit.transpiler import generate_preset_pass_manager
    from qiskit.transpiler.passes import SabreSwap
    from qiskit.primitives import StatevectorEstimator
    from qiskit.providers.fake_provider import GenericBackendV2
    import qiskit.qasm2
    import numpy
    """
    assert _results(code) == set()


def test_dual_message_pulse_specific():
    """A QKT100-specific pulse path also triggers QKT200 via the catch-all."""
    code = """
    from qiskit.pulse.builder import cx
    """
    results = _results(code)
    qkt100 = {r for r in results if "QKT100" in r}
    qkt200 = {r for r in results if "QKT200" in r}
    assert len(qkt100) == 1
    assert len(qkt200) == 1
