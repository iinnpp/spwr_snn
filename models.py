lif_exc = '''
    dV/dt = (gl_e*(E_E_rest - V) + (g_e + ext_drive * g_chr(t,i)*nS)*(E_E_e - V) + g_i*(E_E_i - V))/C_e  + sigma_noise*sqrt(2/(C_e/gl_e))*xi : volt (unless refractory)
    Vt : volt
    Vr : volt
    '''

lif_inh = '''
    dV/dt = (gl_i*(E_I_rest - V) + g_e*(E_I_e - V) + g_i*(E_I_i - V))/C_i  + sigma_noise*sqrt(2/(C_i/gl_i))*xi : volt (unless refractory)
    Vt : volt
    Vr : volt
    '''

syn_EE_biexp = '''
                    dg_e/dt = (invpeak_E_e*s_e - g_e)/tau_d_E_e : siemens
                    ds_e/dt = -s_e/tau_r_E_e : siemens
                    '''

syn_EI_biexp = '''
                    dg_i/dt = (invpeak_E_i*s_i - g_i)/tau_d_E_i : siemens
                    ds_i/dt = -s_i/tau_r_E_i : siemens
                    '''

syn_II_biexp = '''
                    dg_i/dt = (invpeak_I_i*s_i - g_i)/tau_d_I_i : siemens
                    ds_i/dt = -s_i/tau_r_I_i : siemens
                    '''

syn_IE_biexp = '''
                    dg_e/dt = (invpeak_I_e*s_e - g_e)/tau_d_I_e : siemens
                    ds_e/dt = -s_e/tau_r_I_e : siemens
                    '''

fr_threshold = 'V > Vt'

reset = 'V = Vr'

# global excitation and inhibition
# syn_EE_on_pre = 's_e += c_ge * g_peak_E_e'
# syn_EI_on_pre = 's_i += c_gi * g_peak_E_i'
# syn_II_on_pre = 's_i += c_gi * g_peak_I_i'
# syn_IE_on_pre = 's_e += c_ge * g_peak_I_e'

syn_EE_on_pre = 's_e += c_gee * g_peak_E_e'
syn_EI_on_pre = 's_i += c_gei * g_peak_E_i'
syn_II_on_pre = 's_i += c_gii * g_peak_I_i'
# syn_II_on_pre = 's_i += c_gei * g_peak_I_i'
syn_IE_on_pre = 's_e += c_gie * g_peak_I_e'

