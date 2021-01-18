#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 09:39:01 2021

@author: mojtaba
"""
def get_default_folder():
        return '/home/mojtaba/DynaMind-ToolBox/build/output'


import pycd3 as cd3

flow = {'Q': cd3.Flow.flow, 'N': cd3.Flow.concentration}
#Q is flow
#N is nitrogen


_cd3 = cd3.CityDrain3(
    "2005-Jan-01 00:00:00",
    "2006-Jan-01 00:00:00",
    "86400",
    flow
)


#
#


# Register Modules
_cd3.register_native_plugin(
    get_default_folder() + "/libcd3core")
_cd3.register_native_plugin(
    get_default_folder() + "/CD3Modules/libdance4water-nodes")


_cd3.add_node('ConstSource')


# catchment_w_routing = cd3.add_node("Catchment_w_Routing")

# catchment_w_routing.setDoubleParameter(p[0], p[1])

# rain = cd3.add_node("SourceVector")
# rain.setDoubleVectorParameter("source", [0,0,1,2,3,4,5])


# cd3.add_connection(rain, "out", catchment_w_routing, "Rain")

_cd3.init_nodes()

_cd3.start("2005-Jan-01 00:00:00")

print("done")
# cd3.s





