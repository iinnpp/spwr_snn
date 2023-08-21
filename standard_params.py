from brian2.units import *

N_e = 12000
N_i = 200

p_ee = 0.0164
"""initial probability for synapse connection"""
p_ie = 0.1
"""initial probability for synapse connection"""
p_ei = 0.1
"""initial probability for synapse connection"""
p_ii = 0.2
"""initial probability for synapse connection"""

E_E_e = 0.*mV
"""excitatory reversal potential"""
E_E_i = -68.*mV
"""inhibitory reversal potential"""
E_E_rest = -67.*mV
"""resting membrane potential"""
C_e = 275.0*pF
"""excitatory neurons membrane capacitance"""
gl_e = 25.*nS
"""excitatory neurons leak conductance"""
Vt_e = -50. * mV
"""firing threshold for excitatory neurons"""
t_ref_e = 2. * ms
"""refractory period for excitatory neurons"""

E_I_e = 0.*mV
"""excitatory reversal potential"""
E_I_i = -75.*mV
"""inhibitory reversal potential"""
E_I_rest = -65.*mV
"""resting membrane potential"""
C_i = 100.0*pF
"""interneurons membrane capacitance"""
gl_i = 10.*nS
"""interneurons leak conductance"""
Vt_i = -52. * mV
"""firing threshold for interneurons"""
t_ref_i = 1. * ms
"""refractory period for interneurons"""

# Synapse types, only biexp is implemented
syn_cond_mode_ee = 'biexp'
"""Conductance mode of EE synapses, one of exp, biexp"""
syn_cond_mode_ei = 'biexp'
"""Conductance mode of EI synapses, one of exp, biexp"""
syn_cond_mode_ii = 'biexp'
"""Conductance mode of II synapses, one of exp, biexp"""
syn_cond_mode_ie = 'biexp'
"""Conductance mode of IE synapses, one of exp, biexp"""

# "AMPA on pyramidal cells" (E to E)
tau_r_E_e = 0.5 * ms
tau_d_E_e = 1.8 * ms
g_peak_E_e = 0.9 * nS

# "GABA on CA1 pyramidal cells" (I to E)
tau_r_E_i = 0.4 * ms
tau_d_E_i = 2.0 * ms
g_peak_E_i = 9.0 * nS

# "AMPA on interneurons" (E to I)
tau_r_I_e = 0.5*ms
tau_d_I_e = 1.2*ms
g_peak_I_e = 3.0*nS

# "GABA on interneurons" (I to I)
tau_r_I_i = 0.45*ms
tau_d_I_i = 1.2*ms
g_peak_I_i = 5.*nS

# synaptic delay
# this is the propagation delay from the pre-synaptic neuron to the synapse, i.e., the pre-synaptic delay
syn_delay_ee = 1.*ms
syn_delay_ei = 1.*ms
syn_delay_ii = 1.*ms
syn_delay_ie = 1.*ms

sigma_noise = 1.0*mV

dt = 0.01*ms
"""integration time step, same for external input"""

integration_method = 'euler'
"""integration method, by default use euler, for stochastic it will be Euler-Maruyama"""

# global conductance multipliers
c_ge = 1.
"""multiplier for excitatory conductance (for ee and ie)"""
c_gi = 1.
"""multiplier for inhibitory conductance (for ii and ei)"""

# conductance multipliers
c_gee = 1.
"""multiplier for ee """
c_gei = 1.
"""multiplier for ei"""
c_gii = 1.
"""multiplier for ii """
c_gie = 1.
"""multiplier for ie"""

ext_drive = 1.
"""indicates whether the external drive is present, 1 - is present, 0 otherwise """



