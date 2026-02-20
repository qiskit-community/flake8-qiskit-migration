### This file contains all the deprecated/removed paths for Qiskit 2.0.
### Dictionaries are in the form:
###     "qiskit.path": "{} advice to user"
### where `{}` will be replaced with the matched path.
###
### Each path matches all sub-paths, for example `qiskit.thing` will match
### `qiskit.thing.otherthing` in the user's code, unless
### `qiskit.thing.otherthing` appears in EXCEPTIONS_V2.

PULSE_V2 = {
    "qiskit.pulse": "{} has been removed in Qiskit 2.0; see https://quantum.cloud.ibm.com/docs/guides/qiskit-2.0#qiskitpulse",
}

QOBJ_V2 = {
    "qiskit.qobj": "{} has been removed in Qiskit 2.0; use QPY (`qiskit.qpy`) or OpenQASM instead",
}

CLASSICALFUNCTION_V2 = {
    "qiskit.circuit.classicalfunction": "{} has been removed in Qiskit 2.0; use `BitFlipOracleGate` or `PhaseOracleGate` instead",
}

ASSEMBLER_V2 = {
    "qiskit.assembler": "{} has been removed in Qiskit 2.0; the transpilation pipeline handles circuits directly",
    "qiskit.compiler.assemble": "{} has been removed in Qiskit 2.0; backends now accept circuits directly",
    "qiskit.compiler.sequence": "{} has been removed in Qiskit 2.0 as part of Pulse removal; see https://quantum.cloud.ibm.com/docs/guides/qiskit-2.0#qiskitpulse",
    "qiskit.compiler.schedule": "{} has been removed in Qiskit 2.0 as part of Pulse removal; see https://quantum.cloud.ibm.com/docs/guides/qiskit-2.0#qiskitpulse",
}

SCHEDULER_V2 = {
    "qiskit.scheduler": "{} has been removed in Qiskit 2.0 as part of Pulse removal; see https://quantum.cloud.ibm.com/docs/guides/qiskit-2.0#qiskitpulse",
}

PROVIDERS_V2 = {
    "qiskit.providers.BackendV1": "{} has been removed in Qiskit 2.0; migrate to `BackendV2`",
    "qiskit.providers.BackendV2Converter": "{} has been removed in Qiskit 2.0; migrate the input `BackendV1` to `BackendV2`",
    "qiskit.providers.Provider": "{} has been removed in Qiskit 2.0; remove `ProviderV1` as parent class",
    "qiskit.providers.ProviderV1": "{} has been removed in Qiskit 2.0; remove `ProviderV1` as parent class",
    "qiskit.providers.convert_to_target": "{} has been removed in Qiskit 2.0; migrate the input `BackendV1` to `BackendV2` and use its `.target`",
    "qiskit.providers.models": "{} has been removed in Qiskit 2.0; these are not necessary without the removed `BackendV1`. If still using that, migrate to `BackendV2`",
    "qiskit.providers.BackendPropertyError": "{} has been removed in Qiskit 2.0",
    "qiskit.providers.BackendConfigurationError": "{} has been removed in Qiskit 2.0",
    # Fake backends based on BackendV1 (whole module except GenericBackendV2 and utils)
    "qiskit.providers.fake_provider": "{} has been removed in Qiskit 2.0; use `GenericBackendV2` or `qiskit_ibm_runtime.fake_provider`",
}

PRIMITIVES_V2 = {
    "qiskit.primitives.Estimator": "{} (V1 Estimator) has been removed in Qiskit 2.0; use `StatevectorEstimator` instead",
    "qiskit.primitives.Sampler": "{} (V1 Sampler) has been removed in Qiskit 2.0; use `StatevectorSampler` instead",
    "qiskit.primitives.BackendEstimator": "{} (V1 BackendEstimator) has been removed in Qiskit 2.0; use `BackendEstimatorV2` instead",
    "qiskit.primitives.BackendSampler": "{} (V1 BackendSampler) has been removed in Qiskit 2.0; use `BackendSamplerV2` instead",
    "qiskit.primitives.BaseEstimator": "{} (non-versioned V1 alias) has been removed in Qiskit 2.0; replace with `BaseEstimatorV1` or `BaseEstimatorV2`",
    "qiskit.primitives.BaseSampler": "{} (non-versioned V1 alias) has been removed in Qiskit 2.0; replace with `BaseSamplerV1` or `BaseSamplerV2`",
    # Utility functions only used in V1 implementations
    "qiskit.primitives.utils.init_circuit": "{} has been removed in Qiskit 2.0; use `QuantumCircuit.initialize()` instead",
    "qiskit.primitives.utils.init_observable": "{} has been removed in Qiskit 2.0; use the `SparsePauliOp` constructor instead",
    "qiskit.primitives.utils.final_measurement_mapping": "{} has been removed in Qiskit 2.0; use `QuantumCircuit.layout` and `SparsePauliOp.apply_layout()`, or `mthree.utils.final_measurement_mapping`",
}

TRANSPILER_V2 = {
    "qiskit.transpiler.passes.ASAPSchedule": "{} has been removed in Qiskit 2.0; use `ASAPScheduleAnalysis` instead",
    "qiskit.transpiler.passes.ALAPSchedule": "{} has been removed in Qiskit 2.0; use `ALAPScheduleAnalysis` instead",
    "qiskit.transpiler.passes.DynamicalDecoupling": "{} has been removed in Qiskit 2.0; use `PadDynamicalDecoupling` instead",
    "qiskit.transpiler.passes.AlignMeasures": "{} has been removed in Qiskit 2.0; use `ConstrainedReschedule` instead",
    "qiskit.transpiler.passes.CXCancellation": "{} has been removed in Qiskit 2.0; use `InverseCancellation([CXGate()])` instead",
    "qiskit.transpiler.passes.StochasticSwap": "{} has been removed in Qiskit 2.0; use `SabreSwap` instead",
    "qiskit.transpiler.passes.ConvertConditionsToIfOps": "{} has been removed in Qiskit 2.0; `Instruction.condition` no longer exists, use `IfElseOp` instead",
    "qiskit.transpiler.passes.PulseGates": "{} has been removed in Qiskit 2.0 as part of Pulse removal",
    "qiskit.transpiler.passes.ValidatePulseGates": "{} has been removed in Qiskit 2.0 as part of Pulse removal",
    "qiskit.transpiler.passes.RXCalibrationBuilder": "{} has been removed in Qiskit 2.0 as part of Pulse removal",
    "qiskit.transpiler.passes.RZXCalibrationBuilder": "{} has been removed in Qiskit 2.0 as part of Pulse removal",
    "qiskit.transpiler.passes.RZXCalibrationBuilderNoEcho": "{} has been removed in Qiskit 2.0 as part of Pulse removal",
    "qiskit.transpiler.passes.EchoRZXWeylDecomposition": "{} has been removed in Qiskit 2.0 as part of Pulse removal",
    "qiskit.transpiler.passes.NormalizeRXAngle": "{} has been removed in Qiskit 2.0 as part of Pulse removal",
    "qiskit.transpiler.passes.rzx_templates": "{} has been removed in Qiskit 2.0 as part of Pulse removal",
}

RESULT_V2 = {
    "qiskit.result.mitigation": "{} has been removed in Qiskit 2.0; consider an error mitigation library such as `mthree`",
}

VISUALIZATION_V2 = {
    "qiskit.visualization.pulse_drawer": "{} has been removed in Qiskit 2.0 as part of Pulse removal",
    # Note: visualize_transition is NOT removed in 2.0 (still in Qiskit despite deprecation warnings)
}


# These paths are still valid under QKT200 rules; if we hit them, exit early
EXCEPTIONS_V2 = [
    "qiskit.providers.fake_provider.GenericBackendV2",
    "qiskit.providers.fake_provider.utils",
    "qiskit.primitives.StatevectorEstimator",
    "qiskit.primitives.StatevectorSampler",
    "qiskit.primitives.BackendEstimatorV2",
    "qiskit.primitives.BackendSamplerV2",
    "qiskit.primitives.BaseEstimatorV1",
    "qiskit.primitives.BaseSamplerV1",
    "qiskit.primitives.BaseEstimatorV2",
    "qiskit.primitives.BaseSamplerV2",
]

DEPRECATED_PATHS_V2 = (
    PULSE_V2
    | QOBJ_V2
    | CLASSICALFUNCTION_V2
    | ASSEMBLER_V2
    | SCHEDULER_V2
    | PROVIDERS_V2
    | PRIMITIVES_V2
    | TRANSPILER_V2
    | RESULT_V2
    | VISUALIZATION_V2
)
