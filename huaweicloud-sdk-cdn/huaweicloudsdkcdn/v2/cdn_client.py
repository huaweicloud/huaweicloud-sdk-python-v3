# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest
try:
    from huaweicloudsdkcore.invoker.invoker import SyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcdn'")


class CdnClient(Client):
    def __init__(self):
        super(CdnClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcdn.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "CdnClient":
                raise TypeError("client type error, support client type is CdnClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def batch_copy_domain(self, request):
        """批量域名复制

        批量域名复制接口。
         &gt; 将某个加速域名的配置批量复制到其他域名。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCopyDomain
        :type request: :class:`huaweicloudsdkcdn.v2.BatchCopyDomainRequest`
        :rtype: :class:`huaweicloudsdkcdn.v2.BatchCopyDomainResponse`
        """
        http_info = self._batch_copy_domain_http_info(request)
        return self._call_api(**http_info)

    def batch_copy_domain_invoker(self, request):
        http_info = self._batch_copy_domain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_copy_domain_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/cdn/configuration/domains/batch-copy",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCopyDomainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_preheating_tasks(self, request):
        """创建预热缓存任务

        创建预热任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePreheatingTasks
        :type request: :class:`huaweicloudsdkcdn.v2.CreatePreheatingTasksRequest`
        :rtype: :class:`huaweicloudsdkcdn.v2.CreatePreheatingTasksResponse`
        """
        http_info = self._create_preheating_tasks_http_info(request)
        return self._call_api(**http_info)

    def create_preheating_tasks_invoker(self, request):
        http_info = self._create_preheating_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_preheating_tasks_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/cdn/content/preheating-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePreheatingTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_refresh_tasks(self, request):
        """创建刷新缓存任务

        创建刷新缓存任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRefreshTasks
        :type request: :class:`huaweicloudsdkcdn.v2.CreateRefreshTasksRequest`
        :rtype: :class:`huaweicloudsdkcdn.v2.CreateRefreshTasksResponse`
        """
        http_info = self._create_refresh_tasks_http_info(request)
        return self._call_api(**http_info)

    def create_refresh_tasks_invoker(self, request):
        http_info = self._create_refresh_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_refresh_tasks_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/cdn/content/refresh-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRefreshTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def download_region_carrier_excel(self, request):
        """下载区域运营商指标数据表格文件

        - 下载区域运营商指标数据表格文件。
        
        - 支持下载90天内的指标数据表格。
        
        - 时间跨度不能超过31天。
        
        - 起始时间和结束时间，左闭右开。如时间跨度为2022-10-24 00:00:00 到 2022-10-25 00:00:00，表示取 [2022-10-24 00:00:00, 2022-10-25 00:00:00)的统计数据。
        
        - 起始时间、结束时间必须传毫秒级时间戳，起始时间和结束时间必须同时指定。
        
        - 单租户调用频率：10次/min。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadRegionCarrierExcel
        :type request: :class:`huaweicloudsdkcdn.v2.DownloadRegionCarrierExcelRequest`
        :rtype: :class:`huaweicloudsdkcdn.v2.DownloadRegionCarrierExcelResponse`
        """
        http_info = self._download_region_carrier_excel_http_info(request)
        return self._call_api(**http_info)

    def download_region_carrier_excel_invoker(self, request):
        http_info = self._download_region_carrier_excel_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_region_carrier_excel_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/statistics/region-carrier-excel",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadRegionCarrierExcelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))
        if 'country' in local_var_params:
            query_params.append(('country', local_var_params['country']))
        if 'excel_language' in local_var_params:
            query_params.append(('excel_language', local_var_params['excel_language']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'excel_type' in local_var_params:
            query_params.append(('excel_type', local_var_params['excel_type']))
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
        if 'carrier' in local_var_params:
            query_params.append(('carrier', local_var_params['carrier']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def download_statistics_excel(self, request):
        """下载统计指标数据表格文件

        - 下载统计指标数据表格文件。
        
        - 支持下载90天内的指标数据。
        
        - 时间跨度不能超过31天。
        
        - 起始时间和结束时间，左闭右开。如时间跨度为2022-10-24 00:00:00 到 2022-10-25 00:00:00，表示取 [2022-10-24 00:00:00, 2022-10-25 00:00:00)的统计数据。
        
        - 起始时间、结束时间必须传毫秒级时间戳，起始时间和结束时间必须同时指定。
        
        - 单租户调用频率：10次/min。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadStatisticsExcel
        :type request: :class:`huaweicloudsdkcdn.v2.DownloadStatisticsExcelRequest`
        :rtype: :class:`huaweicloudsdkcdn.v2.DownloadStatisticsExcelResponse`
        """
        http_info = self._download_statistics_excel_http_info(request)
        return self._call_api(**http_info)

    def download_statistics_excel_invoker(self, request):
        http_info = self._download_statistics_excel_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_statistics_excel_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/statistics/statistics-excel",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadStatisticsExcelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'excel_language' in local_var_params:
            query_params.append(('excel_language', local_var_params['excel_language']))
        if 'service_area' in local_var_params:
            query_params.append(('service_area', local_var_params['service_area']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'excel_type' in local_var_params:
            query_params.append(('excel_type', local_var_params['excel_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_domains(self, request):
        """查询加速域名

        查询加速域名。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomains
        :type request: :class:`huaweicloudsdkcdn.v2.ListDomainsRequest`
        :rtype: :class:`huaweicloudsdkcdn.v2.ListDomainsResponse`
        """
        http_info = self._list_domains_http_info(request)
        return self._call_api(**http_info)

    def list_domains_invoker(self, request):
        http_info = self._list_domains_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_domains_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/domains",
            "request_type": request.__class__.__name__,
            "response_type": "ListDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'business_type' in local_var_params:
            query_params.append(('business_type', local_var_params['business_type']))
        if 'domain_status' in local_var_params:
            query_params.append(('domain_status', local_var_params['domain_status']))
        if 'service_area' in local_var_params:
            query_params.append(('service_area', local_var_params['service_area']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page_number' in local_var_params:
            query_params.append(('page_number', local_var_params['page_number']))
        if 'show_tags' in local_var_params:
            query_params.append(('show_tags', local_var_params['show_tags']))
        if 'exact_match' in local_var_params:
            query_params.append(('exact_match', local_var_params['exact_match']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def set_charge_modes(self, request):
        """设置用户计费模式

        - 设置用户计费模式。
        
        - 服务区域仅支持mainland_china（国内）
        
        - 计费模式仅支持设置flux（流量），v2及以上客户支持bw（带宽）
        
        - 加速类型仅支持base（基础加速）
        
        - 单租户调用频率：10次/min。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetChargeModes
        :type request: :class:`huaweicloudsdkcdn.v2.SetChargeModesRequest`
        :rtype: :class:`huaweicloudsdkcdn.v2.SetChargeModesResponse`
        """
        http_info = self._set_charge_modes_http_info(request)
        return self._call_api(**http_info)

    def set_charge_modes_invoker(self, request):
        http_info = self._set_charge_modes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_charge_modes_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/cdn/charge/charge-modes",
            "request_type": request.__class__.__name__,
            "response_type": "SetChargeModesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_bandwidth_calc(self, request):
        """查询域名带宽峰值类数据

        - 查询域名带宽峰值类数据。
        
        - 支持查询90天内的数据。
        
        - 查询时间跨度不能超过31天。
        
        - 起始时间和结束时间，左闭右开。如查询2022-10-24 00:00:00 到 2022-10-25 00:00:00 的数据，表示取 [2022-10-24 00:00:00, 2022-10-25 00:00:00)的统计数据。
        
        - 起始时间、结束时间必须传毫秒级时间戳，起始时间和结束时间必须同时指定。
        
        - 流量类指标单位统一为Byte（字节）、带宽类指标单位统一为bit/s（比特/秒）、峰值类指标单位统一为bps（比特率），请求数类和状态码类指标单位统一为次数。用于查询指定域名、指定统计指标的明细数据。
        
        - 单租户调用频率：2次/s。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBandwidthCalc
        :type request: :class:`huaweicloudsdkcdn.v2.ShowBandwidthCalcRequest`
        :rtype: :class:`huaweicloudsdkcdn.v2.ShowBandwidthCalcResponse`
        """
        http_info = self._show_bandwidth_calc_http_info(request)
        return self._call_api(**http_info)

    def show_bandwidth_calc_invoker(self, request):
        http_info = self._show_bandwidth_calc_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_bandwidth_calc_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/statistics/bandwidth-calc",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBandwidthCalcResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'service_area' in local_var_params:
            query_params.append(('service_area', local_var_params['service_area']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'calc_type' in local_var_params:
            query_params.append(('calc_type', local_var_params['calc_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_charge_modes(self, request):
        """查询用户计费模式

        - 查询用户计费模式。
        
        - 服务区域仅支持mainland_china（国内，默认）和outside_mainland_china（海外）
        
        - 计费模式状态支持active（已生效），upcoming（待生效）两种状态，默认为active(已生效)
        
        - 加速类型仅支持base（基础加速）
        
        - 单租户调用频率：5次/s。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowChargeModes
        :type request: :class:`huaweicloudsdkcdn.v2.ShowChargeModesRequest`
        :rtype: :class:`huaweicloudsdkcdn.v2.ShowChargeModesResponse`
        """
        http_info = self._show_charge_modes_http_info(request)
        return self._call_api(**http_info)

    def show_charge_modes_invoker(self, request):
        http_info = self._show_charge_modes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_charge_modes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/charge/charge-modes",
            "request_type": request.__class__.__name__,
            "response_type": "ShowChargeModesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_type' in local_var_params:
            query_params.append(('product_type', local_var_params['product_type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'service_area' in local_var_params:
            query_params.append(('service_area', local_var_params['service_area']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_domain_detail_by_name(self, request):
        """查询加速域名详情

        加速域名详情信息接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainDetailByName
        :type request: :class:`huaweicloudsdkcdn.v2.ShowDomainDetailByNameRequest`
        :rtype: :class:`huaweicloudsdkcdn.v2.ShowDomainDetailByNameResponse`
        """
        http_info = self._show_domain_detail_by_name_http_info(request)
        return self._call_api(**http_info)

    def show_domain_detail_by_name_invoker(self, request):
        http_info = self._show_domain_detail_by_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_domain_detail_by_name_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/configuration/domains/{domain_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainDetailByNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_name' in local_var_params:
            path_params['domain_name'] = local_var_params['domain_name']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_domain_full_config(self, request):
        """查询域名配置接口

        查询域名配置接口，支持查询业务类型、服务范围、备注、IPv6开关、回源方式、回源URL改写、高级回源、Range回源、回源跟随、回源是否校验Etag、回源超时时间、回源请求头、HTTPS配置、TLS版本配置、强制跳转、HSTS、HTTP/2、OCSP Stapling、QUIC、缓存规则、状态码缓存时间、防盗链、IP黑白名单、 Use-Agent黑白名单、URL鉴权配置、远程鉴权配置、IP访问限频、HTTP header配置、自定义错误页面配置、智能压缩、请求限速配置、WebSocket配置、视频拖拽。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainFullConfig
        :type request: :class:`huaweicloudsdkcdn.v2.ShowDomainFullConfigRequest`
        :rtype: :class:`huaweicloudsdkcdn.v2.ShowDomainFullConfigResponse`
        """
        http_info = self._show_domain_full_config_http_info(request)
        return self._call_api(**http_info)

    def show_domain_full_config_invoker(self, request):
        http_info = self._show_domain_full_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_domain_full_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.1/cdn/configuration/domains/{domain_name}/configs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainFullConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_name' in local_var_params:
            path_params['domain_name'] = local_var_params['domain_name']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'show_special_configs' in local_var_params:
            query_params.append(('show_special_configs', local_var_params['show_special_configs']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_domain_location_stats(self, request):
        """按区域运营商查询域名统计数据

        - 支持查询90天内的数据。
        
        - 支持多指标同时查询，不超过5个。
        
        - 最多同时指定20个域名。
        
        - 起始时间和结束时间需要同时指定，左闭右开，毫秒级时间戳，且时间点必须为与查询时间间隔参数匹配的整时刻点。比如查询时间间隔为5分钟时，起始时间和结束时间必须为5分钟整时刻点，如：0分、5分、10分、15分等，如果时间点与时间间隔不匹配，返回数据可能与预期不一致。统一用开始时间表示一个时间段，如：2019-01-24 20:15:00 表示取 [20:15:00, 20:20:00)的统计数据，且左闭右开。
        
        - action取值：location_detail,location_summary
        
        - 流量类指标单位统一为Byte（字节）、带宽类指标单位统一为bit/s（比特/秒）、请求数类和状态码类指标单位统一为次数。用于查询指定域名、指定统计指标的区域运营商明细数据。
        
        - 单租户调用频率：15次/s。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainLocationStats
        :type request: :class:`huaweicloudsdkcdn.v2.ShowDomainLocationStatsRequest`
        :rtype: :class:`huaweicloudsdkcdn.v2.ShowDomainLocationStatsResponse`
        """
        http_info = self._show_domain_location_stats_http_info(request)
        return self._call_api(**http_info)

    def show_domain_location_stats_invoker(self, request):
        http_info = self._show_domain_location_stats_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_domain_location_stats_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/statistics/domain-location-stats",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainLocationStatsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'stat_type' in local_var_params:
            query_params.append(('stat_type', local_var_params['stat_type']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))
        if 'country' in local_var_params:
            query_params.append(('country', local_var_params['country']))
        if 'province' in local_var_params:
            query_params.append(('province', local_var_params['province']))
        if 'isp' in local_var_params:
            query_params.append(('isp', local_var_params['isp']))
        if 'group_by' in local_var_params:
            query_params.append(('group_by', local_var_params['group_by']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_domain_stats(self, request):
        """查询域名统计数据

        - 支持查询90天内的数据。
        
        - 支持多指标同时查询，不超过5个。
        
        - 最多同时指定20个域名。
        
        - 起始时间和结束时间需要同时指定，左闭右开，毫秒级时间戳，且时间点必须为与查询时间间隔参数匹配的整时刻点。比如查询时间间隔为5分钟时，起始时间和结束时间必须为5分钟整时刻点，如：0分、5分、10分、15分等，如果时间点与时间间隔不匹配，返回数据可能与预期不一致。统一用开始时间表示一个时间段，如：2019-01-24 20:15:00 表示取 [20:15:00, 20:20:00)的统计数据，且左闭右开。
        
        - action取值：detail,summary
        
        - 流量类指标单位统一为Byte（字节）、带宽类指标单位统一为bit/s（比特/秒）、请求数类和状态码类指标单位统一为次数。用于查询指定域名、指定统计指标的明细数据。
        
        - 单租户调用频率：15次/s。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainStats
        :type request: :class:`huaweicloudsdkcdn.v2.ShowDomainStatsRequest`
        :rtype: :class:`huaweicloudsdkcdn.v2.ShowDomainStatsResponse`
        """
        http_info = self._show_domain_stats_http_info(request)
        return self._call_api(**http_info)

    def show_domain_stats_invoker(self, request):
        http_info = self._show_domain_stats_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_domain_stats_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/statistics/domain-stats",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainStatsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'stat_type' in local_var_params:
            query_params.append(('stat_type', local_var_params['stat_type']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))
        if 'group_by' in local_var_params:
            query_params.append(('group_by', local_var_params['group_by']))
        if 'service_area' in local_var_params:
            query_params.append(('service_area', local_var_params['service_area']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_history_task_details(self, request):
        """查询刷新预热任务详情

        查询刷新预热任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHistoryTaskDetails
        :type request: :class:`huaweicloudsdkcdn.v2.ShowHistoryTaskDetailsRequest`
        :rtype: :class:`huaweicloudsdkcdn.v2.ShowHistoryTaskDetailsResponse`
        """
        http_info = self._show_history_task_details_http_info(request)
        return self._call_api(**http_info)

    def show_history_task_details_invoker(self, request):
        http_info = self._show_history_task_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_history_task_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/historytasks/{history_tasks_id}/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHistoryTaskDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'history_tasks_id' in local_var_params:
            path_params['history_tasks_id'] = local_var_params['history_tasks_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page_number' in local_var_params:
            query_params.append(('page_number', local_var_params['page_number']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'url' in local_var_params:
            query_params.append(('url', local_var_params['url']))
        if 'create_time' in local_var_params:
            query_params.append(('create_time', local_var_params['create_time']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_history_tasks(self, request):
        """查询刷新预热任务

        查询刷新预热任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHistoryTasks
        :type request: :class:`huaweicloudsdkcdn.v2.ShowHistoryTasksRequest`
        :rtype: :class:`huaweicloudsdkcdn.v2.ShowHistoryTasksResponse`
        """
        http_info = self._show_history_tasks_http_info(request)
        return self._call_api(**http_info)

    def show_history_tasks_invoker(self, request):
        http_info = self._show_history_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_history_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/historytasks",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHistoryTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page_number' in local_var_params:
            query_params.append(('page_number', local_var_params['page_number']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_date' in local_var_params:
            query_params.append(('start_date', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))
        if 'order_field' in local_var_params:
            query_params.append(('order_field', local_var_params['order_field']))
        if 'order_type' in local_var_params:
            query_params.append(('order_type', local_var_params['order_type']))
        if 'file_type' in local_var_params:
            query_params.append(('file_type', local_var_params['file_type']))
        if 'task_type' in local_var_params:
            query_params.append(('task_type', local_var_params['task_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_top_domain_names(self, request):
        """查询TOP域名

        - 查询TOP域名。
        
        - 支持查询90天内的数据。
        
        - 查询时间跨度不能超过1天。
        
        - 起始时间和结束时间，左闭右开，必须同时指定。如查询2022-10-24 00:00:00 到 2022-10-25 00:00:00 的数据，表示取 [2022-10-24 00:00:00, 2022-10-25 00:00:00)的统计数据。
        
        - 起始时间、结束时间必须传整点毫秒级时间戳。
        
        - 流量类指标单位统一为Byte（字节）、带宽类指标单位统一为bit/s（比特/秒）、请求数类和状态码类指标单位统一为次数。用于查询指定域名、指定统计指标的明细数据。
        
        - 单租户调用频率：5次/s。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTopDomainNames
        :type request: :class:`huaweicloudsdkcdn.v2.ShowTopDomainNamesRequest`
        :rtype: :class:`huaweicloudsdkcdn.v2.ShowTopDomainNamesResponse`
        """
        http_info = self._show_top_domain_names_http_info(request)
        return self._call_api(**http_info)

    def show_top_domain_names_invoker(self, request):
        http_info = self._show_top_domain_names_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_top_domain_names_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/cdn/statistics/top-domain-names",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTopDomainNamesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'stat_type' in local_var_params:
            query_params.append(('stat_type', local_var_params['stat_type']))
        if 'service_area' in local_var_params:
            query_params.append(('service_area', local_var_params['service_area']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_top_url(self, request):
        """查询TOP100 URL明细

        - 查询TOP100 URL明细。
        
        - 支持查询90天内的数据。
        
        - 查询跨度不能超过31天。
        
        - 起始时间和结束时间，左闭右开，需要同时指定。如查询2021-10-24 00:00:00 到 2021-10-25 00:00:00 的数据，表示取 [2021-10-24 00:00:00, 2021-10-25 00:00:00)的统计数据。
        
        - 开始时间、结束时间必须传毫秒级时间戳，且必须为凌晨0点整时刻点，如果传的不是凌晨0点整时刻点，返回数据可能与预期不一致。
        
        - 流量类指标单位统一为Byte（字节）、请求数类指标单位统一为次数。用于查询指定域名、指定统计指标的明细数据。
        
        - 单租户调用频率：5次/s。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTopUrl
        :type request: :class:`huaweicloudsdkcdn.v2.ShowTopUrlRequest`
        :rtype: :class:`huaweicloudsdkcdn.v2.ShowTopUrlResponse`
        """
        http_info = self._show_top_url_http_info(request)
        return self._call_api(**http_info)

    def show_top_url_invoker(self, request):
        http_info = self._show_top_url_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_top_url_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/statistics/top-url",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTopUrlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'stat_type' in local_var_params:
            query_params.append(('stat_type', local_var_params['stat_type']))
        if 'service_area' in local_var_params:
            query_params.append(('service_area', local_var_params['service_area']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_url_task_info(self, request):
        """查询刷新预热URL记录

        查询刷新预热URL记录。如需此接口，请提交工单开通。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUrlTaskInfo
        :type request: :class:`huaweicloudsdkcdn.v2.ShowUrlTaskInfoRequest`
        :rtype: :class:`huaweicloudsdkcdn.v2.ShowUrlTaskInfoResponse`
        """
        http_info = self._show_url_task_info_http_info(request)
        return self._call_api(**http_info)

    def show_url_task_info_invoker(self, request):
        http_info = self._show_url_task_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_url_task_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/cdn/contentgateway/url-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUrlTaskInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'url' in local_var_params:
            query_params.append(('url', local_var_params['url']))
        if 'task_type' in local_var_params:
            query_params.append(('task_type', local_var_params['task_type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'file_type' in local_var_params:
            query_params.append(('file_type', local_var_params['file_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_domain_full_config(self, request):
        """修改域名全量配置接口

        修改域名配置接口，支持修改业务类型、服务范围、备注、IPv6开关、回源方式、回源URL改写、高级回源、Range回源、回源跟随、回源是否校验Etag、回源超时时间、回源请求头、HTTPS配置、TLS版本配置、强制跳转、HSTS、HTTP/2、OCSP Stapling、QUIC、缓存规则、状态码缓存时间、防盗链、IP黑白名单、Use-Agent黑白名单、URL鉴权配置、远程鉴权配置、IP访问限频、HTTP header配置、自定义错误页面配置、智能压缩、请求限速配置、WebSocket配置、视频拖拽。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDomainFullConfig
        :type request: :class:`huaweicloudsdkcdn.v2.UpdateDomainFullConfigRequest`
        :rtype: :class:`huaweicloudsdkcdn.v2.UpdateDomainFullConfigResponse`
        """
        http_info = self._update_domain_full_config_http_info(request)
        return self._call_api(**http_info)

    def update_domain_full_config_invoker(self, request):
        http_info = self._update_domain_full_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_domain_full_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.1/cdn/configuration/domains/{domain_name}/configs",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDomainFullConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_name' in local_var_params:
            path_params['domain_name'] = local_var_params['domain_name']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def _call_api(self, **kwargs):
        try:
            return self.do_http_request(**kwargs)
        except TypeError:
            import inspect
            params = inspect.signature(self.do_http_request).parameters
            http_info = {param_name: kwargs.get(param_name) for param_name in params if param_name in kwargs}
            return self.do_http_request(**http_info)

    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, cname=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be placed in the request header.
        :param body: Request body.
        :param post_params: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param cname: Used for obs endpoint.
        :param auth_settings: Auth Settings names for the request.
        :param response_type: Response data type.
        :param response_headers: Header should be added to response data.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param request_type: Request data type.
        :return:
            Return the response directly.
        """
        return self.do_http_request(
            method=method,
            resource_path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
            post_params=post_params,
            cname=cname,
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type)
