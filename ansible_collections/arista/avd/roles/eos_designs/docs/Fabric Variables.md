---
search:
  boost: 2
---

# Fabric Variables

## Evpn Settings

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_ebgp_gateway_multihop</samp>](## "evpn_ebgp_gateway_multihop") | Integer |  | 15 |  | Default of 15, considering a large value to avoid BGP reachability issues in very complex DCI networks.<br>Adapt the value for your specific topology.<br> |
    | [<samp>evpn_ebgp_multihop</samp>](## "evpn_ebgp_multihop") | Integer |  | 3 |  | Default of 3, the recommended value for a 3 stage spine and leaf topology.<br>Set to a higher value to allow for very large and complex topologies.<br> |
    | [<samp>evpn_hostflap_detection</samp>](## "evpn_hostflap_detection") | Dictionary |  |  |  |  |
    | [<samp>evpn_import_pruning</samp>](## "evpn_import_pruning") | Boolean |  | False |  | Enable VPN import pruning (Min. EOS 4.24.2F)<br>The Route Target extended communities carried by incoming VPN paths will<br>be examined. If none of those Route Targets have been configured for import,<br>the path will be immediately discarded<br> |
    | [<samp>evpn_multicast</samp>](## "evpn_multicast") | Boolean |  | False |  | General Configuration required for EVPN Multicast. "evpn_l2_multicast" must also be configured under the Network Services (tenants).<br>Requires "underlay_multicast: true" and IGMP snooping enabled globally (default).<br>For MLAG devices Route Distinguisher must be unique since this feature will create multi-vtep configuration.<br>Warning !!! For Trident3 based platforms i.e 7050X3, 7300X3, 720XP and 722XP<br>  The Following default platform setting will be configured: "platform trident forwarding-table partition flexible exact-match 16384 l2-shared 98304 l3-shared 131072"<br>  All forwarding agents will be restarted when this configuration is applied.<br>  You can tune the settings by overridding the default variable: "platform_settings[platforms].trident_forwarding_table_partition:"<br>  Please contact an Arista representative for help with determining the appropriate values for your environment.<br> |
    | [<samp>evpn_overlay_bgp_rtc</samp>](## "evpn_overlay_bgp_rtc") | Boolean |  | False |  | Enable Route Target Membership Constraint Address Family on EVPN overlay BGP peerings (Min. EOS 4.25.1F)<br>Requires use eBGP as overlay protocol.<br> |
    | [<samp>evpn_prevent_readvertise_to_server</samp>](## "evpn_prevent_readvertise_to_server") | Boolean |  | False |  | Configure route-map on eBGP sessions towards route-servers, where prefixes with the peer's ASN in the AS Path are filtered away.<br>This is very useful in large-scale networks, where convergence will be quicker by not returning all updates received<br>from Route-server-1 to Router-server-2 just for Route-server-2 to throw them away because of AS Path loop detection.<br> |
    | [<samp>evpn_short_esi_prefix</samp>](## "evpn_short_esi_prefix") | String |  | 0000:0000: |  | Configure prefix for "short_esi" values |
    | [<samp>evpn_vlan_aware_bundles</samp>](## "evpn_vlan_aware_bundles") | Boolean |  | False |  | Enable vlan aware bundles for EVPN MAC-VRF<br>Old variable name vxlan_vlan_aware_bundles, supported for backward-compatibility.<br> |

=== "YAML"

    ```yaml
    evpn_ebgp_gateway_multihop: <int>
    evpn_ebgp_multihop: <int>
    evpn_hostflap_detection:
    evpn_import_pruning: <bool>
    evpn_multicast: <bool>
    evpn_overlay_bgp_rtc: <bool>
    evpn_prevent_readvertise_to_server: <bool>
    evpn_short_esi_prefix: <str>
    evpn_vlan_aware_bundles: <bool>
    ```