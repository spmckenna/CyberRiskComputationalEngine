import json
from input_module.cyrce_input import CyrceInput, \
    AttackMotivators, Exploitability, AttackSurface, ThreatActorInput, DirectImpact, Impact, IndirectImpact, \
    CsfFunction, CsfIdentify, CsfProtect, CsfDetect, CsfRespond, CsfRecover, \
    IDAM, IDBE, IDGV, IDRA, IDRM, IDSC, PRAC, PRAT, PRDS, PRIP, PRMA, \
    PRPT, DEAE, DECM, DEDP, RSRP, RSCO, RSAN, RSMI, RSIM, RCRP, RCIM, RCCO, AT_1, AT_2, AT_3, AT_4, RA_1, RA_2, RA_3, \
    RA_5, RA_7, RA_9, AT, RA, Sp80053_
from api_resources.cyrce_resource import CyrceResource
from core_module.model_main import run_cyrce
from core_module.analysis import run_ttp_coverage_metric
from scenario_module.ScenarioModel import Scenario

if __name__ == '__main__':

    attackMotivators = AttackMotivators(2.5, 2.5, 2.5, 2.5)
    attackSurface = AttackSurface(3, 2)
    exploitability = Exploitability(2)
    threatActorInput = ThreatActorInput(determination='high', resources='organization', sophistication='advanced')
    directImpact = DirectImpact(3, 3, 2, 1)
    indirectImpact = IndirectImpact(3, 3, 2, 1)
    impact = Impact(directImpact, indirectImpact)
    scenario = Scenario(attackAction='hacking', attackThreatType='threatactor', attackTarget='label:Crown Jewel',
                        attackLossType='c', attackIndustry='information', attackGeography='na', orgSize="large")
    # scenario = Scenario()  # know nothing case; posterior is prior
    identify = CsfIdentify(IDAM=IDAM(0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8),
                           IDBE=IDBE(0.8, 0.8, 0.8, 0.8, 0.8, 0.8),
                           IDGV=IDGV(0.8, 0.8, 0.8, 0.8, 0.8),
                           IDRA=IDRA(0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8),
                           IDRM=IDRM(0.8, 0.8, 0.8, 0.8),
                           IDSC=IDSC(0.8, 0.8, 0.8, 0.8, 0.8, 0.8),
                           value=0.5
                           )
    protect = CsfProtect(value=0.5,
                         PRAC=PRAC(value=0.4, PRAC1=0.4, PRAC2=0.4, PRAC3=0.4, PRAC4=0.4, PRAC5=0.4, PRAC6=0.4,
                                   PRAC7=0.4),
                         PRAT=PRAT(value=0.4, PRAT1=0.4, PRAT2=0.4, PRAT3=0.4, PRAT4=0.4, PRAT5=0.4),
                         PRDS=PRDS(value=0.4, PRDS1=0.4, PRDS2=0.4, PRDS3=0.4, PRDS4=0.4, PRDS5=0.4, PRDS6=0.4,
                                   PRDS7=0.4, PRDS8=0.4),
                         PRIP=PRIP(value=0.4, PRIP1=0.4, PRIP2=0.4, PRIP3=0.4, PRIP4=0.4, PRIP5=0.4, PRIP6=0.4,
                                   PRIP7=0.4, PRIP8=0.4,
                                   PRIP9=0.4, PRIP10=0.4, PRIP11=0.4, PRIP12=0.4),
                         PRMA=PRMA(value=0.4, PRMA1=0.4, PRMA2=0.4),
                         PRPT=PRPT(value=0.4, PRPT1=0.4, PRPT2=0.4, PRPT3=0.4, PRPT4=0.4, PRPT5=0.4)
                         )
    detect = CsfDetect(value=0.5,
                       DEAE=DEAE(value=0.4, DEAE1=0.4, DEAE2=0.4, DEAE3=0.4, DEAE4=0.4, DEAE5=0.4),
                       DECM=DECM(value=0.4, DECM1=0.4, DECM2=0.4, DECM3=0.4, DECM4=0.4, DECM5=0.4, DECM6=0.4, DECM7=0.4,
                                 DECM8=0.4),
                       DEDP=DEDP(value=0.4, DEDP1=0.4, DEDP2=0.4, DEDP3=0.4, DEDP4=0.4, DEDP5=0.4))
    respond = CsfRespond(value=0.46,
                         RSRP=RSRP(value=0.426, RSRP1=0.426),
                         RSCO=RSCO(value=0.426, RSCO1=0.426, RSCO2=0.426, RSCO3=0.426, RSCO4=0.426, RSCO5=0.426),
                         RSAN=RSAN(value=0.426, RSAN1=0.426, RSAN2=0.426, RSAN3=0.426, RSAN4=0.426, RSAN5=0.426),
                         RSMI=RSMI(value=0.426, RSMI1=0.426, RSMI2=0.426, RSMI3=0.426),
                         RSIM=RSIM(value=0.426, RSIM1=0.426, RSIM2=0.426))
    recover = CsfRecover(value=0.46,
                         RCRP=RCRP(value=0.426, RCRP1=0.426),
                         RCIM=RCIM(value=0.426, RCIM1=0.426, RCIM2=0.426),
                         RCCO=RCCO(value=0.426, RCCO1=0.426, RCCO2=0.426, RCCO3=0.426)
                         )
    csf = CsfFunction(identify=identify,
                      protect=protect,
                      detect=detect,
                      respond=respond,
                      recover=recover)
    ra_1 = RA_1(value=0.25)
    ra_2 = RA_2(value=0.75)
    ra_3 = RA_3(value=0.5)
    ra_5 = RA_5(value=0.25)
    ra_7 = RA_7(value=0.75)
    ra_9 = RA_9(value=0.5)
    ra = RA(value=0.5, RA_1=ra_1.value, RA_2=ra_2.value, RA_3=ra_3.value, RA_5=ra_5.value, RA_7=ra_7.value, RA_9=ra_9.value)
    at_1 = AT_1(value=0.25)
    at_2 = AT_2(value=0.5)
    at_3 = AT_3(value=0.75)
    at_4 = AT_4(value=0.5)
    at = RA(value=0.5, RA_1=ra_1.value, RA_2=ra_2.value, RA_3=ra_3.value, RA_5=ra_5.value,
            RA_7=ra_7.value, RA_9=ra_9)
    sp80053 = Sp80053_(RA=ra, AT=at)

    control_mode = 'csf'
    if control_mode == 'csf':
        sp80053 = None
    else:
        csf = None
    cyrce_input = CyrceInput(attackMotivators=attackMotivators,
                             attackSurface=attackSurface,
                             exploitability=exploitability,
                             threatActorInput=threatActorInput,
                             impact=impact,
                             csf=csf, sp80053=sp80053,
                             scenario=scenario)
    output_csf = run_cyrce(cyrce_input=cyrce_input, control_mode=control_mode)
    #output_80053 = run_cyrce(cyrce_input=cyrce_input, control_mode='sp80053')

    # mimic api
    with open('request.json') as file:
        json_data = json.load(file)

    cy_res = CyrceResource()

    #output_csf_api = run_cyrce(control_mode='csf', cyrce_input=cy_res.json_to_input(json_data)).reprJSON()
    #output_80053_api = run_cyrce(control_mode='sp80053', cyrce_input=cy_res.json_to_input(json_data)).reprJSON()

   # with open('../sp80053.json') as file:
    #    json_data = json.load(file)
    #attack_coverage_metric = run_ttp_coverage_metric(scenario=1, ctrls_dict=json_data)
    #print(round(attack_coverage_metric, 1))