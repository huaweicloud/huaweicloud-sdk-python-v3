# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CaseReportDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_success_rate_check_point': 'float',
        'alias': 'str',
        'average_resp_time': 'float',
        'average_resp_time_check_point': 'float',
        'average_resp_time_check_res': 'bool',
        'avg_network_traffic': 'float',
        'avg_rec_bytes': 'int',
        'avg_rec_bytes_check_point': 'float',
        'avg_rec_bytes_check_res': 'bool',
        'avg_sent_bytes': 'int',
        'avg_sent_bytes_check_point': 'float',
        'avg_sent_bytes_check_res': 'bool',
        'avg_tran_resp_time': 'float',
        'avg_tran_resp_time_check_point': 'float',
        'avg_tran_resp_time_check_res': 'bool',
        'aw_id': 'str',
        'case_uri': 'str',
        'checkpoint_result': 'bool',
        'cpu_usage': 'float',
        'cpu_usage_avg': 'float',
        'cpu_usage_avg_check_point': 'float',
        'cpu_usage_avg_check_res': 'bool',
        'cpu_usage_check_point': 'float',
        'cpu_usage_check_res': 'bool',
        'create_time': 'str',
        'current_thread_num': 'int',
        'datum_type': 'int',
        'dcs_latency_avg': 'float',
        'dcs_latency_avg_check_point': 'float',
        'dcs_latency_avg_check_res': 'bool',
        'dcs_latency_max': 'float',
        'dcs_latency_max_check_point': 'float',
        'dcs_latency_max_check_res': 'bool',
        'dcs_latency_min': 'float',
        'dcs_latency_min_check_point': 'float',
        'dcs_latency_min_check_res': 'bool',
        'detail_id': 'str',
        'disk_read': 'float',
        'disk_read_avg': 'float',
        'disk_read_avg_check_point': 'float',
        'disk_read_avg_check_res': 'bool',
        'disk_read_check_point': 'float',
        'disk_read_check_res': 'bool',
        'disk_usage': 'float',
        'disk_usage_avg': 'float',
        'disk_usage_avg_check_point': 'float',
        'disk_usage_avg_check_res': 'bool',
        'disk_usage_check_point': 'float',
        'disk_usage_check_res': 'bool',
        'disk_write': 'float',
        'disk_write_avg': 'float',
        'disk_write_avg_check_point': 'float',
        'disk_write_avg_check_res': 'bool',
        'disk_write_check_point': 'float',
        'disk_write_check_res': 'bool',
        'duration': 'int',
        'end_time': 'str',
        'error_count': 'int',
        'error_events_count': 'int',
        'failed_assert': 'int',
        'failed_others': 'int',
        'failed_parsed': 'int',
        'failed_reason': 'str',
        'failed_refused': 'int',
        'failed_timeout': 'int',
        'id': 'str',
        'is_aw': 'bool',
        'iteration_uri': 'str',
        'kpi_monitor': 'str',
        'max': 'int',
        'max_avg_time': 'float',
        'max_avg_time_check_point': 'float',
        'max_avg_time_check_res': 'bool',
        'max_network_traffic': 'int',
        'max_rec_bytes': 'int',
        'max_rec_bytes_check_point': 'float',
        'max_rec_bytes_check_res': 'bool',
        'max_resp_time': 'int',
        'max_resp_time_check_point': 'float',
        'max_resp_time_check_res': 'bool',
        'max_rps': 'int',
        'max_sent_bytes': 'int',
        'max_sent_bytes_check_point': 'float',
        'max_sent_bytes_check_res': 'bool',
        'max_success_rate': 'float',
        'max_success_rate_check_res': 'bool',
        'max_thread_num': 'float',
        'max_thread_num_check_point': 'float',
        'max_thread_num_check_res': 'bool',
        'max_tps': 'float',
        'max_tps_check_point': 'float',
        'max_tps_check_res': 'bool',
        'max_tran_resp_time': 'float',
        'max_tran_resp_time_check_point': 'float',
        'max_tran_resp_time_check_res': 'bool',
        'memory_usage': 'float',
        'memory_usage_avg': 'float',
        'memory_usage_avg_check_point': 'float',
        'memory_usage_avg_check_res': 'bool',
        'memory_usage_check_point': 'float',
        'memory_usage_check_res': 'bool',
        'min': 'int',
        'min_network_traffic': 'int',
        'mode': 'str',
        'monitor_peak_time': 'float',
        'monitor_peak_time_check_point': 'float',
        'monitor_peak_time_check_res': 'bool',
        'monitor_result': 'float',
        'monitor_result_check_point': 'float',
        'monitor_result_check_res': 'bool',
        'name': 'str',
        'network_read': 'float',
        'network_read_avg': 'float',
        'network_read_avg_check_point': 'float',
        'network_read_avg_check_res': 'bool',
        'network_read_check_point': 'float',
        'network_read_check_res': 'bool',
        'network_write': 'float',
        'network_write_avg': 'float',
        'network_write_avg_check_point': 'float',
        'network_write_avg_check_res': 'bool',
        'network_write_check_point': 'float',
        'network_write_check_res': 'bool',
        'peak_load_status': 'float',
        'peak_load_status_check_point': 'float',
        'peak_load_status_check_res': 'bool',
        'peak_metric': 'PeakMetric',
        'project_id': 'str',
        'protocols': 'list[str]',
        'requests': 'int',
        'result': 'int',
        'result_log': 'str',
        'round': 'int',
        'save_all_data': 'bool',
        'service_id': 'str',
        'stage': 'int',
        'start_time': 'str',
        'status': 'int',
        'streaming_media_vo': 'StreamingMediaReport',
        'success_count': 'int',
        'success_rate': 'int',
        'success_rate_check_point': 'float',
        'success_rate_check_res': 'bool',
        'sum1xx': 'int',
        'sum2xx': 'int',
        'sum3xx': 'int',
        'sum4xx': 'int',
        'sum5xx': 'int',
        'task_id': 'str',
        'task_name': 'str',
        'task_project_id': 'str',
        'task_status': 'int',
        'test_case_uri': 'str',
        'tp50': 'int',
        'tp50_check_point': 'float',
        'tp50_check_res': 'bool',
        'tp75': 'int',
        'tp75_check_point': 'float',
        'tp75_check_res': 'bool',
        'tp85': 'int',
        'tp85_check_point': 'float',
        'tp85_check_res': 'bool',
        'tp90': 'int',
        'tp90_check_point': 'float',
        'tp90_check_res': 'bool',
        'tp95': 'int',
        'tp95_check_point': 'float',
        'tp95_check_res': 'bool',
        'tp99': 'int',
        'tp999': 'int',
        'tp9999': 'int',
        'tp9999_check_point': 'float',
        'tp9999_check_res': 'bool',
        'tp999_check_point': 'float',
        'tp999_check_res': 'bool',
        'tp99_check_point': 'float',
        'tp99_check_res': 'bool',
        'tps': 'float',
        'tps_check_point': 'float',
        'tps_check_res': 'bool',
        'tran_tps': 'float',
        'tran_tps_check_point': 'float',
        'tran_tps_check_res': 'bool',
        'transaction_id': 'str',
        'transaction_success': 'float',
        'transactions': 'float',
        'transactions_check_point': 'float',
        'transactions_check_res': 'bool',
        'update_time': 'str',
        'url': 'str',
        'user_concur': 'int',
        'version_uri': 'str'
    }

    attribute_map = {
        'max_success_rate_check_point': 'MaxSuccessRateCheckPoint',
        'alias': 'alias',
        'average_resp_time': 'averageRespTime',
        'average_resp_time_check_point': 'averageRespTimeCheckPoint',
        'average_resp_time_check_res': 'averageRespTimeCheckRes',
        'avg_network_traffic': 'avgNetworkTraffic',
        'avg_rec_bytes': 'avgRecBytes',
        'avg_rec_bytes_check_point': 'avgRecBytesCheckPoint',
        'avg_rec_bytes_check_res': 'avgRecBytesCheckRes',
        'avg_sent_bytes': 'avgSentBytes',
        'avg_sent_bytes_check_point': 'avgSentBytesCheckPoint',
        'avg_sent_bytes_check_res': 'avgSentBytesCheckRes',
        'avg_tran_resp_time': 'avgTranRespTime',
        'avg_tran_resp_time_check_point': 'avgTranRespTimeCheckPoint',
        'avg_tran_resp_time_check_res': 'avgTranRespTimeCheckRes',
        'aw_id': 'awId',
        'case_uri': 'caseUri',
        'checkpoint_result': 'checkpointResult',
        'cpu_usage': 'cpuUsage',
        'cpu_usage_avg': 'cpuUsageAvg',
        'cpu_usage_avg_check_point': 'cpuUsageAvgCheckPoint',
        'cpu_usage_avg_check_res': 'cpuUsageAvgCheckRes',
        'cpu_usage_check_point': 'cpuUsageCheckPoint',
        'cpu_usage_check_res': 'cpuUsageCheckRes',
        'create_time': 'createTime',
        'current_thread_num': 'currentThreadNum',
        'datum_type': 'datumType',
        'dcs_latency_avg': 'dcsLatencyAvg',
        'dcs_latency_avg_check_point': 'dcsLatencyAvgCheckPoint',
        'dcs_latency_avg_check_res': 'dcsLatencyAvgCheckRes',
        'dcs_latency_max': 'dcsLatencyMax',
        'dcs_latency_max_check_point': 'dcsLatencyMaxCheckPoint',
        'dcs_latency_max_check_res': 'dcsLatencyMaxCheckRes',
        'dcs_latency_min': 'dcsLatencyMin',
        'dcs_latency_min_check_point': 'dcsLatencyMinCheckPoint',
        'dcs_latency_min_check_res': 'dcsLatencyMinCheckRes',
        'detail_id': 'detailId',
        'disk_read': 'diskRead',
        'disk_read_avg': 'diskReadAvg',
        'disk_read_avg_check_point': 'diskReadAvgCheckPoint',
        'disk_read_avg_check_res': 'diskReadAvgCheckRes',
        'disk_read_check_point': 'diskReadCheckPoint',
        'disk_read_check_res': 'diskReadCheckRes',
        'disk_usage': 'diskUsage',
        'disk_usage_avg': 'diskUsageAvg',
        'disk_usage_avg_check_point': 'diskUsageAvgCheckPoint',
        'disk_usage_avg_check_res': 'diskUsageAvgCheckRes',
        'disk_usage_check_point': 'diskUsageCheckPoint',
        'disk_usage_check_res': 'diskUsageCheckRes',
        'disk_write': 'diskWrite',
        'disk_write_avg': 'diskWriteAvg',
        'disk_write_avg_check_point': 'diskWriteAvgCheckPoint',
        'disk_write_avg_check_res': 'diskWriteAvgCheckRes',
        'disk_write_check_point': 'diskWriteCheckPoint',
        'disk_write_check_res': 'diskWriteCheckRes',
        'duration': 'duration',
        'end_time': 'endTime',
        'error_count': 'errorCount',
        'error_events_count': 'errorEventsCount',
        'failed_assert': 'failedAssert',
        'failed_others': 'failedOthers',
        'failed_parsed': 'failedParsed',
        'failed_reason': 'failedReason',
        'failed_refused': 'failedRefused',
        'failed_timeout': 'failedTimeout',
        'id': 'id',
        'is_aw': 'isAW',
        'iteration_uri': 'iterationUri',
        'kpi_monitor': 'kpiMonitor',
        'max': 'max',
        'max_avg_time': 'maxAvgTime',
        'max_avg_time_check_point': 'maxAvgTimeCheckPoint',
        'max_avg_time_check_res': 'maxAvgTimeCheckRes',
        'max_network_traffic': 'maxNetworkTraffic',
        'max_rec_bytes': 'maxRecBytes',
        'max_rec_bytes_check_point': 'maxRecBytesCheckPoint',
        'max_rec_bytes_check_res': 'maxRecBytesCheckRes',
        'max_resp_time': 'maxRespTime',
        'max_resp_time_check_point': 'maxRespTimeCheckPoint',
        'max_resp_time_check_res': 'maxRespTimeCheckRes',
        'max_rps': 'maxRps',
        'max_sent_bytes': 'maxSentBytes',
        'max_sent_bytes_check_point': 'maxSentBytesCheckPoint',
        'max_sent_bytes_check_res': 'maxSentBytesCheckRes',
        'max_success_rate': 'maxSuccessRate',
        'max_success_rate_check_res': 'maxSuccessRateCheckRes',
        'max_thread_num': 'maxThreadNum',
        'max_thread_num_check_point': 'maxThreadNumCheckPoint',
        'max_thread_num_check_res': 'maxThreadNumCheckRes',
        'max_tps': 'maxTps',
        'max_tps_check_point': 'maxTpsCheckPoint',
        'max_tps_check_res': 'maxTpsCheckRes',
        'max_tran_resp_time': 'maxTranRespTime',
        'max_tran_resp_time_check_point': 'maxTranRespTimeCheckPoint',
        'max_tran_resp_time_check_res': 'maxTranRespTimeCheckRes',
        'memory_usage': 'memoryUsage',
        'memory_usage_avg': 'memoryUsageAvg',
        'memory_usage_avg_check_point': 'memoryUsageAvgCheckPoint',
        'memory_usage_avg_check_res': 'memoryUsageAvgCheckRes',
        'memory_usage_check_point': 'memoryUsageCheckPoint',
        'memory_usage_check_res': 'memoryUsageCheckRes',
        'min': 'min',
        'min_network_traffic': 'minNetworkTraffic',
        'mode': 'mode',
        'monitor_peak_time': 'monitorPeakTime',
        'monitor_peak_time_check_point': 'monitorPeakTimeCheckPoint',
        'monitor_peak_time_check_res': 'monitorPeakTimeCheckRes',
        'monitor_result': 'monitorResult',
        'monitor_result_check_point': 'monitorResultCheckPoint',
        'monitor_result_check_res': 'monitorResultCheckRes',
        'name': 'name',
        'network_read': 'networkRead',
        'network_read_avg': 'networkReadAvg',
        'network_read_avg_check_point': 'networkReadAvgCheckPoint',
        'network_read_avg_check_res': 'networkReadAvgCheckRes',
        'network_read_check_point': 'networkReadCheckPoint',
        'network_read_check_res': 'networkReadCheckRes',
        'network_write': 'networkWrite',
        'network_write_avg': 'networkWriteAvg',
        'network_write_avg_check_point': 'networkWriteAvgCheckPoint',
        'network_write_avg_check_res': 'networkWriteAvgCheckRes',
        'network_write_check_point': 'networkWriteCheckPoint',
        'network_write_check_res': 'networkWriteCheckRes',
        'peak_load_status': 'peakLoadStatus',
        'peak_load_status_check_point': 'peakLoadStatusCheckPoint',
        'peak_load_status_check_res': 'peakLoadStatusCheckRes',
        'peak_metric': 'peakMetric',
        'project_id': 'projectId',
        'protocols': 'protocols',
        'requests': 'requests',
        'result': 'result',
        'result_log': 'resultLog',
        'round': 'round',
        'save_all_data': 'saveAllData',
        'service_id': 'serviceId',
        'stage': 'stage',
        'start_time': 'startTime',
        'status': 'status',
        'streaming_media_vo': 'streamingMediaVo',
        'success_count': 'successCount',
        'success_rate': 'successRate',
        'success_rate_check_point': 'successRateCheckPoint',
        'success_rate_check_res': 'successRateCheckRes',
        'sum1xx': 'sum1xx',
        'sum2xx': 'sum2xx',
        'sum3xx': 'sum3xx',
        'sum4xx': 'sum4xx',
        'sum5xx': 'sum5xx',
        'task_id': 'taskId',
        'task_name': 'taskName',
        'task_project_id': 'taskProjectId',
        'task_status': 'taskStatus',
        'test_case_uri': 'testCaseUri',
        'tp50': 'tp50',
        'tp50_check_point': 'tp50CheckPoint',
        'tp50_check_res': 'tp50CheckRes',
        'tp75': 'tp75',
        'tp75_check_point': 'tp75CheckPoint',
        'tp75_check_res': 'tp75CheckRes',
        'tp85': 'tp85',
        'tp85_check_point': 'tp85CheckPoint',
        'tp85_check_res': 'tp85CheckRes',
        'tp90': 'tp90',
        'tp90_check_point': 'tp90CheckPoint',
        'tp90_check_res': 'tp90CheckRes',
        'tp95': 'tp95',
        'tp95_check_point': 'tp95CheckPoint',
        'tp95_check_res': 'tp95CheckRes',
        'tp99': 'tp99',
        'tp999': 'tp999',
        'tp9999': 'tp9999',
        'tp9999_check_point': 'tp9999CheckPoint',
        'tp9999_check_res': 'tp9999CheckRes',
        'tp999_check_point': 'tp999CheckPoint',
        'tp999_check_res': 'tp999CheckRes',
        'tp99_check_point': 'tp99CheckPoint',
        'tp99_check_res': 'tp99CheckRes',
        'tps': 'tps',
        'tps_check_point': 'tpsCheckPoint',
        'tps_check_res': 'tpsCheckRes',
        'tran_tps': 'tranTPS',
        'tran_tps_check_point': 'tranTPSCheckPoint',
        'tran_tps_check_res': 'tranTPSCheckRes',
        'transaction_id': 'transactionId',
        'transaction_success': 'transactionSuccess',
        'transactions': 'transactions',
        'transactions_check_point': 'transactionsCheckPoint',
        'transactions_check_res': 'transactionsCheckRes',
        'update_time': 'updateTime',
        'url': 'url',
        'user_concur': 'userConcur',
        'version_uri': 'versionUri'
    }

    def __init__(self, max_success_rate_check_point=None, alias=None, average_resp_time=None, average_resp_time_check_point=None, average_resp_time_check_res=None, avg_network_traffic=None, avg_rec_bytes=None, avg_rec_bytes_check_point=None, avg_rec_bytes_check_res=None, avg_sent_bytes=None, avg_sent_bytes_check_point=None, avg_sent_bytes_check_res=None, avg_tran_resp_time=None, avg_tran_resp_time_check_point=None, avg_tran_resp_time_check_res=None, aw_id=None, case_uri=None, checkpoint_result=None, cpu_usage=None, cpu_usage_avg=None, cpu_usage_avg_check_point=None, cpu_usage_avg_check_res=None, cpu_usage_check_point=None, cpu_usage_check_res=None, create_time=None, current_thread_num=None, datum_type=None, dcs_latency_avg=None, dcs_latency_avg_check_point=None, dcs_latency_avg_check_res=None, dcs_latency_max=None, dcs_latency_max_check_point=None, dcs_latency_max_check_res=None, dcs_latency_min=None, dcs_latency_min_check_point=None, dcs_latency_min_check_res=None, detail_id=None, disk_read=None, disk_read_avg=None, disk_read_avg_check_point=None, disk_read_avg_check_res=None, disk_read_check_point=None, disk_read_check_res=None, disk_usage=None, disk_usage_avg=None, disk_usage_avg_check_point=None, disk_usage_avg_check_res=None, disk_usage_check_point=None, disk_usage_check_res=None, disk_write=None, disk_write_avg=None, disk_write_avg_check_point=None, disk_write_avg_check_res=None, disk_write_check_point=None, disk_write_check_res=None, duration=None, end_time=None, error_count=None, error_events_count=None, failed_assert=None, failed_others=None, failed_parsed=None, failed_reason=None, failed_refused=None, failed_timeout=None, id=None, is_aw=None, iteration_uri=None, kpi_monitor=None, max=None, max_avg_time=None, max_avg_time_check_point=None, max_avg_time_check_res=None, max_network_traffic=None, max_rec_bytes=None, max_rec_bytes_check_point=None, max_rec_bytes_check_res=None, max_resp_time=None, max_resp_time_check_point=None, max_resp_time_check_res=None, max_rps=None, max_sent_bytes=None, max_sent_bytes_check_point=None, max_sent_bytes_check_res=None, max_success_rate=None, max_success_rate_check_res=None, max_thread_num=None, max_thread_num_check_point=None, max_thread_num_check_res=None, max_tps=None, max_tps_check_point=None, max_tps_check_res=None, max_tran_resp_time=None, max_tran_resp_time_check_point=None, max_tran_resp_time_check_res=None, memory_usage=None, memory_usage_avg=None, memory_usage_avg_check_point=None, memory_usage_avg_check_res=None, memory_usage_check_point=None, memory_usage_check_res=None, min=None, min_network_traffic=None, mode=None, monitor_peak_time=None, monitor_peak_time_check_point=None, monitor_peak_time_check_res=None, monitor_result=None, monitor_result_check_point=None, monitor_result_check_res=None, name=None, network_read=None, network_read_avg=None, network_read_avg_check_point=None, network_read_avg_check_res=None, network_read_check_point=None, network_read_check_res=None, network_write=None, network_write_avg=None, network_write_avg_check_point=None, network_write_avg_check_res=None, network_write_check_point=None, network_write_check_res=None, peak_load_status=None, peak_load_status_check_point=None, peak_load_status_check_res=None, peak_metric=None, project_id=None, protocols=None, requests=None, result=None, result_log=None, round=None, save_all_data=None, service_id=None, stage=None, start_time=None, status=None, streaming_media_vo=None, success_count=None, success_rate=None, success_rate_check_point=None, success_rate_check_res=None, sum1xx=None, sum2xx=None, sum3xx=None, sum4xx=None, sum5xx=None, task_id=None, task_name=None, task_project_id=None, task_status=None, test_case_uri=None, tp50=None, tp50_check_point=None, tp50_check_res=None, tp75=None, tp75_check_point=None, tp75_check_res=None, tp85=None, tp85_check_point=None, tp85_check_res=None, tp90=None, tp90_check_point=None, tp90_check_res=None, tp95=None, tp95_check_point=None, tp95_check_res=None, tp99=None, tp999=None, tp9999=None, tp9999_check_point=None, tp9999_check_res=None, tp999_check_point=None, tp999_check_res=None, tp99_check_point=None, tp99_check_res=None, tps=None, tps_check_point=None, tps_check_res=None, tran_tps=None, tran_tps_check_point=None, tran_tps_check_res=None, transaction_id=None, transaction_success=None, transactions=None, transactions_check_point=None, transactions_check_res=None, update_time=None, url=None, user_concur=None, version_uri=None):
        """CaseReportDetail

        The model defined in huaweicloud sdk

        :param max_success_rate_check_point: 最大成功率检查点
        :type max_success_rate_check_point: float
        :param alias: 别名
        :type alias: str
        :param average_resp_time: 平均响应时间
        :type average_resp_time: float
        :param average_resp_time_check_point: 平均响应时间检查点
        :type average_resp_time_check_point: float
        :param average_resp_time_check_res: 平均响应时间检查结果
        :type average_resp_time_check_res: bool
        :param avg_network_traffic: 平均带宽
        :type avg_network_traffic: float
        :param avg_rec_bytes: 平均下行带宽
        :type avg_rec_bytes: int
        :param avg_rec_bytes_check_point: 平均下行带宽检查点
        :type avg_rec_bytes_check_point: float
        :param avg_rec_bytes_check_res: 平均下行带宽检查结果
        :type avg_rec_bytes_check_res: bool
        :param avg_sent_bytes: 平均上行带宽
        :type avg_sent_bytes: int
        :param avg_sent_bytes_check_point: 平均上行带宽检查点
        :type avg_sent_bytes_check_point: float
        :param avg_sent_bytes_check_res: 平均上行带宽检查结果
        :type avg_sent_bytes_check_res: bool
        :param avg_tran_resp_time: 事务平均响应时间
        :type avg_tran_resp_time: float
        :param avg_tran_resp_time_check_point: 事务平均响应时间检查点
        :type avg_tran_resp_time_check_point: float
        :param avg_tran_resp_time_check_res: 事务平均响应时间检查结果
        :type avg_tran_resp_time_check_res: bool
        :param aw_id: awId
        :type aw_id: str
        :param case_uri: 用例Uri
        :type case_uri: str
        :param checkpoint_result: 所有检查点结果的汇总结果
        :type checkpoint_result: bool
        :param cpu_usage: cpu最大使用率
        :type cpu_usage: float
        :param cpu_usage_avg: cpu平均使用率
        :type cpu_usage_avg: float
        :param cpu_usage_avg_check_point: cpu平均使用率检查点
        :type cpu_usage_avg_check_point: float
        :param cpu_usage_avg_check_res: cpu平均使用率检查结果
        :type cpu_usage_avg_check_res: bool
        :param cpu_usage_check_point: cpu最大使用率检查点
        :type cpu_usage_check_point: float
        :param cpu_usage_check_res: cpu最大使用率检查结果
        :type cpu_usage_check_res: bool
        :param create_time: 创建时间
        :type create_time: str
        :param current_thread_num: 最大并发数
        :type current_thread_num: int
        :param datum_type: 数据类型(case/aw/transaction)
        :type datum_type: int
        :param dcs_latency_avg: dcs平均时延
        :type dcs_latency_avg: float
        :param dcs_latency_avg_check_point: dcs平均时延检查点
        :type dcs_latency_avg_check_point: float
        :param dcs_latency_avg_check_res: dcs平均时延检查结果
        :type dcs_latency_avg_check_res: bool
        :param dcs_latency_max: dcs最大时延
        :type dcs_latency_max: float
        :param dcs_latency_max_check_point: dcs最大时延检查点·
        :type dcs_latency_max_check_point: float
        :param dcs_latency_max_check_res: dcs最大时延检查结果
        :type dcs_latency_max_check_res: bool
        :param dcs_latency_min: dcs最小时延
        :type dcs_latency_min: float
        :param dcs_latency_min_check_point: dcs最小时延检查点
        :type dcs_latency_min_check_point: float
        :param dcs_latency_min_check_res: dcs最小时延检查结果
        :type dcs_latency_min_check_res: bool
        :param detail_id: 用例/aw/事务在数据库中dc_case_aw表的主键ID
        :type detail_id: str
        :param disk_read: 磁盘最大读取速度
        :type disk_read: float
        :param disk_read_avg: 磁盘平均读取速度
        :type disk_read_avg: float
        :param disk_read_avg_check_point: 磁盘平均读取速度检查点
        :type disk_read_avg_check_point: float
        :param disk_read_avg_check_res: 磁盘平均读取速度检查结果
        :type disk_read_avg_check_res: bool
        :param disk_read_check_point: 磁盘最大读取速度检查点
        :type disk_read_check_point: float
        :param disk_read_check_res: 磁盘最大读取速度检查结果
        :type disk_read_check_res: bool
        :param disk_usage: 磁盘最大使用率
        :type disk_usage: float
        :param disk_usage_avg: 磁盘平均使用率
        :type disk_usage_avg: float
        :param disk_usage_avg_check_point: 磁盘平均使用率检查点
        :type disk_usage_avg_check_point: float
        :param disk_usage_avg_check_res: 磁盘平均使用率检查结果
        :type disk_usage_avg_check_res: bool
        :param disk_usage_check_point: 磁盘最大使用率检查点
        :type disk_usage_check_point: float
        :param disk_usage_check_res: 磁盘最大使用率检查结果
        :type disk_usage_check_res: bool
        :param disk_write: 磁盘最大写入速度
        :type disk_write: float
        :param disk_write_avg: 磁盘平均写入速度
        :type disk_write_avg: float
        :param disk_write_avg_check_point: 磁盘平均写入速度检查点
        :type disk_write_avg_check_point: float
        :param disk_write_avg_check_res: 磁盘平均写入速度检查结果
        :type disk_write_avg_check_res: bool
        :param disk_write_check_point: 磁盘最大写入速度检查点
        :type disk_write_check_point: float
        :param disk_write_check_res: 磁盘最大写入速度检查结果
        :type disk_write_check_res: bool
        :param duration: 运行时长
        :type duration: int
        :param end_time: 结束时间
        :type end_time: str
        :param error_count: 错误数
        :type error_count: int
        :param error_events_count: 错误事件数
        :type error_events_count: int
        :param failed_assert: 断言失败数
        :type failed_assert: int
        :param failed_others: 其他失败数
        :type failed_others: int
        :param failed_parsed: 解析失败数
        :type failed_parsed: int
        :param failed_reason: 失败原因
        :type failed_reason: str
        :param failed_refused: 连接拒绝失败数
        :type failed_refused: int
        :param failed_timeout: 连接超时失败数
        :type failed_timeout: int
        :param id: 用例在数据库中dc_testcase表的主键id
        :type id: str
        :param is_aw: 是否是aw
        :type is_aw: bool
        :param iteration_uri: 迭代uri
        :type iteration_uri: str
        :param kpi_monitor: 来源于设计服务的监控数据
        :type kpi_monitor: str
        :param max: 最大响应时间
        :type max: int
        :param max_avg_time: 平均响应时间
        :type max_avg_time: float
        :param max_avg_time_check_point: 平均响应时间检查点
        :type max_avg_time_check_point: float
        :param max_avg_time_check_res: 平均响应时间检查结果
        :type max_avg_time_check_res: bool
        :param max_network_traffic: 流量峰值
        :type max_network_traffic: int
        :param max_rec_bytes: 最大下行带宽
        :type max_rec_bytes: int
        :param max_rec_bytes_check_point: 最大下行带宽检查点
        :type max_rec_bytes_check_point: float
        :param max_rec_bytes_check_res: 最大下行带宽检查结果
        :type max_rec_bytes_check_res: bool
        :param max_resp_time: 最大响应时间
        :type max_resp_time: int
        :param max_resp_time_check_point: 最大响应时间检查点
        :type max_resp_time_check_point: float
        :param max_resp_time_check_res: 最大响应时间检查结果
        :type max_resp_time_check_res: bool
        :param max_rps: 最大RPS
        :type max_rps: int
        :param max_sent_bytes: 最大上行带宽
        :type max_sent_bytes: int
        :param max_sent_bytes_check_point: 最大上行带宽检查点
        :type max_sent_bytes_check_point: float
        :param max_sent_bytes_check_res: 最大上行带宽检查结果
        :type max_sent_bytes_check_res: bool
        :param max_success_rate: 最大成功率
        :type max_success_rate: float
        :param max_success_rate_check_res: 最大成功率检查结果
        :type max_success_rate_check_res: bool
        :param max_thread_num: 最大线程数
        :type max_thread_num: float
        :param max_thread_num_check_point: 最大线程数检查点
        :type max_thread_num_check_point: float
        :param max_thread_num_check_res: 最大线程数检查结果
        :type max_thread_num_check_res: bool
        :param max_tps: 最大TPS
        :type max_tps: float
        :param max_tps_check_point: 最大TPS检查点
        :type max_tps_check_point: float
        :param max_tps_check_res: 最大TPS检查结果
        :type max_tps_check_res: bool
        :param max_tran_resp_time: 最大事务响应时间
        :type max_tran_resp_time: float
        :param max_tran_resp_time_check_point: 最大事务响应时间检查点
        :type max_tran_resp_time_check_point: float
        :param max_tran_resp_time_check_res: 最大事务响应时间检查结果
        :type max_tran_resp_time_check_res: bool
        :param memory_usage: 最大内存使用率
        :type memory_usage: float
        :param memory_usage_avg: 平均内存使用率
        :type memory_usage_avg: float
        :param memory_usage_avg_check_point: 平均内存使用率检查点
        :type memory_usage_avg_check_point: float
        :param memory_usage_avg_check_res: 平均内存使用率检查结果
        :type memory_usage_avg_check_res: bool
        :param memory_usage_check_point: 最大内存使用率检查点
        :type memory_usage_check_point: float
        :param memory_usage_check_res: 最大内存使用率检查结果
        :type memory_usage_check_res: bool
        :param min: 最小响应时间
        :type min: int
        :param min_network_traffic: 流量谷值
        :type min_network_traffic: int
        :param mode: 压力模式
        :type mode: str
        :param monitor_peak_time: 监控峰值时间
        :type monitor_peak_time: float
        :param monitor_peak_time_check_point: 监控峰值时间检查点
        :type monitor_peak_time_check_point: float
        :param monitor_peak_time_check_res: 监控峰值时间检查结果
        :type monitor_peak_time_check_res: bool
        :param monitor_result: 监控结果
        :type monitor_result: float
        :param monitor_result_check_point: 监控结果检查点
        :type monitor_result_check_point: float
        :param monitor_result_check_res: 监控结果检查结果
        :type monitor_result_check_res: bool
        :param name: 用例/aw/事务名
        :type name: str
        :param network_read: 网络最大接收数据速度
        :type network_read: float
        :param network_read_avg: 网络平均接收数据速度
        :type network_read_avg: float
        :param network_read_avg_check_point: 网络平均接收数据速度检查点
        :type network_read_avg_check_point: float
        :param network_read_avg_check_res: 网络平均接收数据速度检查结果
        :type network_read_avg_check_res: bool
        :param network_read_check_point: 网络最大接收数据速度检查点
        :type network_read_check_point: float
        :param network_read_check_res: 网络最大接收数据速度检查结果
        :type network_read_check_res: bool
        :param network_write: 网络最大写入数据速度
        :type network_write: float
        :param network_write_avg: 网络平均写入数据速度
        :type network_write_avg: float
        :param network_write_avg_check_point: 网络平均写入数据速度检查点
        :type network_write_avg_check_point: float
        :param network_write_avg_check_res: 网络平均写入数据速度检查结果
        :type network_write_avg_check_res: bool
        :param network_write_check_point: 网络最大写入数据速度检查点
        :type network_write_check_point: float
        :param network_write_check_res: 网络最大写入数据速度检查结果
        :type network_write_check_res: bool
        :param peak_load_status: 峰值负载状态
        :type peak_load_status: float
        :param peak_load_status_check_point: 峰值负载状态检查点
        :type peak_load_status_check_point: float
        :param peak_load_status_check_res: 峰值负载状态检查结果
        :type peak_load_status_check_res: bool
        :param peak_metric: 
        :type peak_metric: :class:`huaweicloudsdkcpts.v1.PeakMetric`
        :param project_id: 工程ID
        :type project_id: str
        :param protocols: 协议
        :type protocols: list[str]
        :param requests: 请求数
        :type requests: int
        :param result: 用例结果
        :type result: int
        :param result_log: 用例结果日志
        :type result_log: str
        :param round: 执行轮次
        :type round: int
        :param save_all_data: 是否存储全量数据到CSS
        :type save_all_data: bool
        :param service_id: 服务ID
        :type service_id: str
        :param stage: 阶段
        :type stage: int
        :param start_time: 开始时间
        :type start_time: str
        :param status: 任务状态
        :type status: int
        :param streaming_media_vo: 
        :type streaming_media_vo: :class:`huaweicloudsdkcpts.v1.StreamingMediaReport`
        :param success_count: 成功数
        :type success_count: int
        :param success_rate: 成功率
        :type success_rate: int
        :param success_rate_check_point: 成功率检查点
        :type success_rate_check_point: float
        :param success_rate_check_res: 成功率检查结果
        :type success_rate_check_res: bool
        :param sum1xx: 1XX响应码数量
        :type sum1xx: int
        :param sum2xx: 2XX响应码数量
        :type sum2xx: int
        :param sum3xx: 3XX响应码数量
        :type sum3xx: int
        :param sum4xx: 4XX响应码数量
        :type sum4xx: int
        :param sum5xx: 5XX响应码数量
        :type sum5xx: int
        :param task_id: 任务ID
        :type task_id: str
        :param task_name: 任务名
        :type task_name: str
        :param task_project_id: 任务项目ID
        :type task_project_id: str
        :param task_status: 任务状态
        :type task_status: int
        :param test_case_uri: 用例基线uri
        :type test_case_uri: str
        :param tp50: TP50
        :type tp50: int
        :param tp50_check_point: TP50检查点
        :type tp50_check_point: float
        :param tp50_check_res: TP50检查结果
        :type tp50_check_res: bool
        :param tp75: TP75
        :type tp75: int
        :param tp75_check_point: TP75检查点
        :type tp75_check_point: float
        :param tp75_check_res: TP75检查结果
        :type tp75_check_res: bool
        :param tp85: TP85
        :type tp85: int
        :param tp85_check_point: TP85检查点
        :type tp85_check_point: float
        :param tp85_check_res: TP85检查结果
        :type tp85_check_res: bool
        :param tp90: TP90
        :type tp90: int
        :param tp90_check_point: TP90检查点
        :type tp90_check_point: float
        :param tp90_check_res: TP90检查结果
        :type tp90_check_res: bool
        :param tp95: TP95
        :type tp95: int
        :param tp95_check_point: TP95检查点
        :type tp95_check_point: float
        :param tp95_check_res: TP95检查结果
        :type tp95_check_res: bool
        :param tp99: TP99
        :type tp99: int
        :param tp999: TP99.9
        :type tp999: int
        :param tp9999: TP99.99
        :type tp9999: int
        :param tp9999_check_point: TP99.99检查点
        :type tp9999_check_point: float
        :param tp9999_check_res: TP99.99检查结果
        :type tp9999_check_res: bool
        :param tp999_check_point: TP99.9检查点
        :type tp999_check_point: float
        :param tp999_check_res: TP99.9检查结果
        :type tp999_check_res: bool
        :param tp99_check_point: TP99检查点
        :type tp99_check_point: float
        :param tp99_check_res: TP99检查结果
        :type tp99_check_res: bool
        :param tps: TPS
        :type tps: float
        :param tps_check_point: TPS检查点
        :type tps_check_point: float
        :param tps_check_res: TPS检查结果
        :type tps_check_res: bool
        :param tran_tps: 平均TPS
        :type tran_tps: float
        :param tran_tps_check_point: 平均TPS检查点
        :type tran_tps_check_point: float
        :param tran_tps_check_res: 平均TPS检查结果
        :type tran_tps_check_res: bool
        :param transaction_id: 事务ID
        :type transaction_id: str
        :param transaction_success: 事务成功数
        :type transaction_success: float
        :param transactions: 事务数
        :type transactions: float
        :param transactions_check_point: 事务数检查点
        :type transactions_check_point: float
        :param transactions_check_res: 事务数检查结果
        :type transactions_check_res: bool
        :param update_time: 更新时间
        :type update_time: str
        :param url: aw的http url
        :type url: str
        :param user_concur: 反应实时vuser数据
        :type user_concur: int
        :param version_uri: 分支uri
        :type version_uri: str
        """
        
        

        self._max_success_rate_check_point = None
        self._alias = None
        self._average_resp_time = None
        self._average_resp_time_check_point = None
        self._average_resp_time_check_res = None
        self._avg_network_traffic = None
        self._avg_rec_bytes = None
        self._avg_rec_bytes_check_point = None
        self._avg_rec_bytes_check_res = None
        self._avg_sent_bytes = None
        self._avg_sent_bytes_check_point = None
        self._avg_sent_bytes_check_res = None
        self._avg_tran_resp_time = None
        self._avg_tran_resp_time_check_point = None
        self._avg_tran_resp_time_check_res = None
        self._aw_id = None
        self._case_uri = None
        self._checkpoint_result = None
        self._cpu_usage = None
        self._cpu_usage_avg = None
        self._cpu_usage_avg_check_point = None
        self._cpu_usage_avg_check_res = None
        self._cpu_usage_check_point = None
        self._cpu_usage_check_res = None
        self._create_time = None
        self._current_thread_num = None
        self._datum_type = None
        self._dcs_latency_avg = None
        self._dcs_latency_avg_check_point = None
        self._dcs_latency_avg_check_res = None
        self._dcs_latency_max = None
        self._dcs_latency_max_check_point = None
        self._dcs_latency_max_check_res = None
        self._dcs_latency_min = None
        self._dcs_latency_min_check_point = None
        self._dcs_latency_min_check_res = None
        self._detail_id = None
        self._disk_read = None
        self._disk_read_avg = None
        self._disk_read_avg_check_point = None
        self._disk_read_avg_check_res = None
        self._disk_read_check_point = None
        self._disk_read_check_res = None
        self._disk_usage = None
        self._disk_usage_avg = None
        self._disk_usage_avg_check_point = None
        self._disk_usage_avg_check_res = None
        self._disk_usage_check_point = None
        self._disk_usage_check_res = None
        self._disk_write = None
        self._disk_write_avg = None
        self._disk_write_avg_check_point = None
        self._disk_write_avg_check_res = None
        self._disk_write_check_point = None
        self._disk_write_check_res = None
        self._duration = None
        self._end_time = None
        self._error_count = None
        self._error_events_count = None
        self._failed_assert = None
        self._failed_others = None
        self._failed_parsed = None
        self._failed_reason = None
        self._failed_refused = None
        self._failed_timeout = None
        self._id = None
        self._is_aw = None
        self._iteration_uri = None
        self._kpi_monitor = None
        self._max = None
        self._max_avg_time = None
        self._max_avg_time_check_point = None
        self._max_avg_time_check_res = None
        self._max_network_traffic = None
        self._max_rec_bytes = None
        self._max_rec_bytes_check_point = None
        self._max_rec_bytes_check_res = None
        self._max_resp_time = None
        self._max_resp_time_check_point = None
        self._max_resp_time_check_res = None
        self._max_rps = None
        self._max_sent_bytes = None
        self._max_sent_bytes_check_point = None
        self._max_sent_bytes_check_res = None
        self._max_success_rate = None
        self._max_success_rate_check_res = None
        self._max_thread_num = None
        self._max_thread_num_check_point = None
        self._max_thread_num_check_res = None
        self._max_tps = None
        self._max_tps_check_point = None
        self._max_tps_check_res = None
        self._max_tran_resp_time = None
        self._max_tran_resp_time_check_point = None
        self._max_tran_resp_time_check_res = None
        self._memory_usage = None
        self._memory_usage_avg = None
        self._memory_usage_avg_check_point = None
        self._memory_usage_avg_check_res = None
        self._memory_usage_check_point = None
        self._memory_usage_check_res = None
        self._min = None
        self._min_network_traffic = None
        self._mode = None
        self._monitor_peak_time = None
        self._monitor_peak_time_check_point = None
        self._monitor_peak_time_check_res = None
        self._monitor_result = None
        self._monitor_result_check_point = None
        self._monitor_result_check_res = None
        self._name = None
        self._network_read = None
        self._network_read_avg = None
        self._network_read_avg_check_point = None
        self._network_read_avg_check_res = None
        self._network_read_check_point = None
        self._network_read_check_res = None
        self._network_write = None
        self._network_write_avg = None
        self._network_write_avg_check_point = None
        self._network_write_avg_check_res = None
        self._network_write_check_point = None
        self._network_write_check_res = None
        self._peak_load_status = None
        self._peak_load_status_check_point = None
        self._peak_load_status_check_res = None
        self._peak_metric = None
        self._project_id = None
        self._protocols = None
        self._requests = None
        self._result = None
        self._result_log = None
        self._round = None
        self._save_all_data = None
        self._service_id = None
        self._stage = None
        self._start_time = None
        self._status = None
        self._streaming_media_vo = None
        self._success_count = None
        self._success_rate = None
        self._success_rate_check_point = None
        self._success_rate_check_res = None
        self._sum1xx = None
        self._sum2xx = None
        self._sum3xx = None
        self._sum4xx = None
        self._sum5xx = None
        self._task_id = None
        self._task_name = None
        self._task_project_id = None
        self._task_status = None
        self._test_case_uri = None
        self._tp50 = None
        self._tp50_check_point = None
        self._tp50_check_res = None
        self._tp75 = None
        self._tp75_check_point = None
        self._tp75_check_res = None
        self._tp85 = None
        self._tp85_check_point = None
        self._tp85_check_res = None
        self._tp90 = None
        self._tp90_check_point = None
        self._tp90_check_res = None
        self._tp95 = None
        self._tp95_check_point = None
        self._tp95_check_res = None
        self._tp99 = None
        self._tp999 = None
        self._tp9999 = None
        self._tp9999_check_point = None
        self._tp9999_check_res = None
        self._tp999_check_point = None
        self._tp999_check_res = None
        self._tp99_check_point = None
        self._tp99_check_res = None
        self._tps = None
        self._tps_check_point = None
        self._tps_check_res = None
        self._tran_tps = None
        self._tran_tps_check_point = None
        self._tran_tps_check_res = None
        self._transaction_id = None
        self._transaction_success = None
        self._transactions = None
        self._transactions_check_point = None
        self._transactions_check_res = None
        self._update_time = None
        self._url = None
        self._user_concur = None
        self._version_uri = None
        self.discriminator = None

        if max_success_rate_check_point is not None:
            self.max_success_rate_check_point = max_success_rate_check_point
        if alias is not None:
            self.alias = alias
        if average_resp_time is not None:
            self.average_resp_time = average_resp_time
        if average_resp_time_check_point is not None:
            self.average_resp_time_check_point = average_resp_time_check_point
        if average_resp_time_check_res is not None:
            self.average_resp_time_check_res = average_resp_time_check_res
        if avg_network_traffic is not None:
            self.avg_network_traffic = avg_network_traffic
        if avg_rec_bytes is not None:
            self.avg_rec_bytes = avg_rec_bytes
        if avg_rec_bytes_check_point is not None:
            self.avg_rec_bytes_check_point = avg_rec_bytes_check_point
        if avg_rec_bytes_check_res is not None:
            self.avg_rec_bytes_check_res = avg_rec_bytes_check_res
        if avg_sent_bytes is not None:
            self.avg_sent_bytes = avg_sent_bytes
        if avg_sent_bytes_check_point is not None:
            self.avg_sent_bytes_check_point = avg_sent_bytes_check_point
        if avg_sent_bytes_check_res is not None:
            self.avg_sent_bytes_check_res = avg_sent_bytes_check_res
        if avg_tran_resp_time is not None:
            self.avg_tran_resp_time = avg_tran_resp_time
        if avg_tran_resp_time_check_point is not None:
            self.avg_tran_resp_time_check_point = avg_tran_resp_time_check_point
        if avg_tran_resp_time_check_res is not None:
            self.avg_tran_resp_time_check_res = avg_tran_resp_time_check_res
        if aw_id is not None:
            self.aw_id = aw_id
        if case_uri is not None:
            self.case_uri = case_uri
        if checkpoint_result is not None:
            self.checkpoint_result = checkpoint_result
        if cpu_usage is not None:
            self.cpu_usage = cpu_usage
        if cpu_usage_avg is not None:
            self.cpu_usage_avg = cpu_usage_avg
        if cpu_usage_avg_check_point is not None:
            self.cpu_usage_avg_check_point = cpu_usage_avg_check_point
        if cpu_usage_avg_check_res is not None:
            self.cpu_usage_avg_check_res = cpu_usage_avg_check_res
        if cpu_usage_check_point is not None:
            self.cpu_usage_check_point = cpu_usage_check_point
        if cpu_usage_check_res is not None:
            self.cpu_usage_check_res = cpu_usage_check_res
        if create_time is not None:
            self.create_time = create_time
        if current_thread_num is not None:
            self.current_thread_num = current_thread_num
        if datum_type is not None:
            self.datum_type = datum_type
        if dcs_latency_avg is not None:
            self.dcs_latency_avg = dcs_latency_avg
        if dcs_latency_avg_check_point is not None:
            self.dcs_latency_avg_check_point = dcs_latency_avg_check_point
        if dcs_latency_avg_check_res is not None:
            self.dcs_latency_avg_check_res = dcs_latency_avg_check_res
        if dcs_latency_max is not None:
            self.dcs_latency_max = dcs_latency_max
        if dcs_latency_max_check_point is not None:
            self.dcs_latency_max_check_point = dcs_latency_max_check_point
        if dcs_latency_max_check_res is not None:
            self.dcs_latency_max_check_res = dcs_latency_max_check_res
        if dcs_latency_min is not None:
            self.dcs_latency_min = dcs_latency_min
        if dcs_latency_min_check_point is not None:
            self.dcs_latency_min_check_point = dcs_latency_min_check_point
        if dcs_latency_min_check_res is not None:
            self.dcs_latency_min_check_res = dcs_latency_min_check_res
        if detail_id is not None:
            self.detail_id = detail_id
        if disk_read is not None:
            self.disk_read = disk_read
        if disk_read_avg is not None:
            self.disk_read_avg = disk_read_avg
        if disk_read_avg_check_point is not None:
            self.disk_read_avg_check_point = disk_read_avg_check_point
        if disk_read_avg_check_res is not None:
            self.disk_read_avg_check_res = disk_read_avg_check_res
        if disk_read_check_point is not None:
            self.disk_read_check_point = disk_read_check_point
        if disk_read_check_res is not None:
            self.disk_read_check_res = disk_read_check_res
        if disk_usage is not None:
            self.disk_usage = disk_usage
        if disk_usage_avg is not None:
            self.disk_usage_avg = disk_usage_avg
        if disk_usage_avg_check_point is not None:
            self.disk_usage_avg_check_point = disk_usage_avg_check_point
        if disk_usage_avg_check_res is not None:
            self.disk_usage_avg_check_res = disk_usage_avg_check_res
        if disk_usage_check_point is not None:
            self.disk_usage_check_point = disk_usage_check_point
        if disk_usage_check_res is not None:
            self.disk_usage_check_res = disk_usage_check_res
        if disk_write is not None:
            self.disk_write = disk_write
        if disk_write_avg is not None:
            self.disk_write_avg = disk_write_avg
        if disk_write_avg_check_point is not None:
            self.disk_write_avg_check_point = disk_write_avg_check_point
        if disk_write_avg_check_res is not None:
            self.disk_write_avg_check_res = disk_write_avg_check_res
        if disk_write_check_point is not None:
            self.disk_write_check_point = disk_write_check_point
        if disk_write_check_res is not None:
            self.disk_write_check_res = disk_write_check_res
        if duration is not None:
            self.duration = duration
        if end_time is not None:
            self.end_time = end_time
        if error_count is not None:
            self.error_count = error_count
        if error_events_count is not None:
            self.error_events_count = error_events_count
        if failed_assert is not None:
            self.failed_assert = failed_assert
        if failed_others is not None:
            self.failed_others = failed_others
        if failed_parsed is not None:
            self.failed_parsed = failed_parsed
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if failed_refused is not None:
            self.failed_refused = failed_refused
        if failed_timeout is not None:
            self.failed_timeout = failed_timeout
        if id is not None:
            self.id = id
        if is_aw is not None:
            self.is_aw = is_aw
        if iteration_uri is not None:
            self.iteration_uri = iteration_uri
        if kpi_monitor is not None:
            self.kpi_monitor = kpi_monitor
        if max is not None:
            self.max = max
        if max_avg_time is not None:
            self.max_avg_time = max_avg_time
        if max_avg_time_check_point is not None:
            self.max_avg_time_check_point = max_avg_time_check_point
        if max_avg_time_check_res is not None:
            self.max_avg_time_check_res = max_avg_time_check_res
        if max_network_traffic is not None:
            self.max_network_traffic = max_network_traffic
        if max_rec_bytes is not None:
            self.max_rec_bytes = max_rec_bytes
        if max_rec_bytes_check_point is not None:
            self.max_rec_bytes_check_point = max_rec_bytes_check_point
        if max_rec_bytes_check_res is not None:
            self.max_rec_bytes_check_res = max_rec_bytes_check_res
        if max_resp_time is not None:
            self.max_resp_time = max_resp_time
        if max_resp_time_check_point is not None:
            self.max_resp_time_check_point = max_resp_time_check_point
        if max_resp_time_check_res is not None:
            self.max_resp_time_check_res = max_resp_time_check_res
        if max_rps is not None:
            self.max_rps = max_rps
        if max_sent_bytes is not None:
            self.max_sent_bytes = max_sent_bytes
        if max_sent_bytes_check_point is not None:
            self.max_sent_bytes_check_point = max_sent_bytes_check_point
        if max_sent_bytes_check_res is not None:
            self.max_sent_bytes_check_res = max_sent_bytes_check_res
        if max_success_rate is not None:
            self.max_success_rate = max_success_rate
        if max_success_rate_check_res is not None:
            self.max_success_rate_check_res = max_success_rate_check_res
        if max_thread_num is not None:
            self.max_thread_num = max_thread_num
        if max_thread_num_check_point is not None:
            self.max_thread_num_check_point = max_thread_num_check_point
        if max_thread_num_check_res is not None:
            self.max_thread_num_check_res = max_thread_num_check_res
        if max_tps is not None:
            self.max_tps = max_tps
        if max_tps_check_point is not None:
            self.max_tps_check_point = max_tps_check_point
        if max_tps_check_res is not None:
            self.max_tps_check_res = max_tps_check_res
        if max_tran_resp_time is not None:
            self.max_tran_resp_time = max_tran_resp_time
        if max_tran_resp_time_check_point is not None:
            self.max_tran_resp_time_check_point = max_tran_resp_time_check_point
        if max_tran_resp_time_check_res is not None:
            self.max_tran_resp_time_check_res = max_tran_resp_time_check_res
        if memory_usage is not None:
            self.memory_usage = memory_usage
        if memory_usage_avg is not None:
            self.memory_usage_avg = memory_usage_avg
        if memory_usage_avg_check_point is not None:
            self.memory_usage_avg_check_point = memory_usage_avg_check_point
        if memory_usage_avg_check_res is not None:
            self.memory_usage_avg_check_res = memory_usage_avg_check_res
        if memory_usage_check_point is not None:
            self.memory_usage_check_point = memory_usage_check_point
        if memory_usage_check_res is not None:
            self.memory_usage_check_res = memory_usage_check_res
        if min is not None:
            self.min = min
        if min_network_traffic is not None:
            self.min_network_traffic = min_network_traffic
        if mode is not None:
            self.mode = mode
        if monitor_peak_time is not None:
            self.monitor_peak_time = monitor_peak_time
        if monitor_peak_time_check_point is not None:
            self.monitor_peak_time_check_point = monitor_peak_time_check_point
        if monitor_peak_time_check_res is not None:
            self.monitor_peak_time_check_res = monitor_peak_time_check_res
        if monitor_result is not None:
            self.monitor_result = monitor_result
        if monitor_result_check_point is not None:
            self.monitor_result_check_point = monitor_result_check_point
        if monitor_result_check_res is not None:
            self.monitor_result_check_res = monitor_result_check_res
        if name is not None:
            self.name = name
        if network_read is not None:
            self.network_read = network_read
        if network_read_avg is not None:
            self.network_read_avg = network_read_avg
        if network_read_avg_check_point is not None:
            self.network_read_avg_check_point = network_read_avg_check_point
        if network_read_avg_check_res is not None:
            self.network_read_avg_check_res = network_read_avg_check_res
        if network_read_check_point is not None:
            self.network_read_check_point = network_read_check_point
        if network_read_check_res is not None:
            self.network_read_check_res = network_read_check_res
        if network_write is not None:
            self.network_write = network_write
        if network_write_avg is not None:
            self.network_write_avg = network_write_avg
        if network_write_avg_check_point is not None:
            self.network_write_avg_check_point = network_write_avg_check_point
        if network_write_avg_check_res is not None:
            self.network_write_avg_check_res = network_write_avg_check_res
        if network_write_check_point is not None:
            self.network_write_check_point = network_write_check_point
        if network_write_check_res is not None:
            self.network_write_check_res = network_write_check_res
        if peak_load_status is not None:
            self.peak_load_status = peak_load_status
        if peak_load_status_check_point is not None:
            self.peak_load_status_check_point = peak_load_status_check_point
        if peak_load_status_check_res is not None:
            self.peak_load_status_check_res = peak_load_status_check_res
        if peak_metric is not None:
            self.peak_metric = peak_metric
        if project_id is not None:
            self.project_id = project_id
        if protocols is not None:
            self.protocols = protocols
        if requests is not None:
            self.requests = requests
        if result is not None:
            self.result = result
        if result_log is not None:
            self.result_log = result_log
        if round is not None:
            self.round = round
        if save_all_data is not None:
            self.save_all_data = save_all_data
        if service_id is not None:
            self.service_id = service_id
        if stage is not None:
            self.stage = stage
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if streaming_media_vo is not None:
            self.streaming_media_vo = streaming_media_vo
        if success_count is not None:
            self.success_count = success_count
        if success_rate is not None:
            self.success_rate = success_rate
        if success_rate_check_point is not None:
            self.success_rate_check_point = success_rate_check_point
        if success_rate_check_res is not None:
            self.success_rate_check_res = success_rate_check_res
        if sum1xx is not None:
            self.sum1xx = sum1xx
        if sum2xx is not None:
            self.sum2xx = sum2xx
        if sum3xx is not None:
            self.sum3xx = sum3xx
        if sum4xx is not None:
            self.sum4xx = sum4xx
        if sum5xx is not None:
            self.sum5xx = sum5xx
        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if task_project_id is not None:
            self.task_project_id = task_project_id
        if task_status is not None:
            self.task_status = task_status
        if test_case_uri is not None:
            self.test_case_uri = test_case_uri
        if tp50 is not None:
            self.tp50 = tp50
        if tp50_check_point is not None:
            self.tp50_check_point = tp50_check_point
        if tp50_check_res is not None:
            self.tp50_check_res = tp50_check_res
        if tp75 is not None:
            self.tp75 = tp75
        if tp75_check_point is not None:
            self.tp75_check_point = tp75_check_point
        if tp75_check_res is not None:
            self.tp75_check_res = tp75_check_res
        if tp85 is not None:
            self.tp85 = tp85
        if tp85_check_point is not None:
            self.tp85_check_point = tp85_check_point
        if tp85_check_res is not None:
            self.tp85_check_res = tp85_check_res
        if tp90 is not None:
            self.tp90 = tp90
        if tp90_check_point is not None:
            self.tp90_check_point = tp90_check_point
        if tp90_check_res is not None:
            self.tp90_check_res = tp90_check_res
        if tp95 is not None:
            self.tp95 = tp95
        if tp95_check_point is not None:
            self.tp95_check_point = tp95_check_point
        if tp95_check_res is not None:
            self.tp95_check_res = tp95_check_res
        if tp99 is not None:
            self.tp99 = tp99
        if tp999 is not None:
            self.tp999 = tp999
        if tp9999 is not None:
            self.tp9999 = tp9999
        if tp9999_check_point is not None:
            self.tp9999_check_point = tp9999_check_point
        if tp9999_check_res is not None:
            self.tp9999_check_res = tp9999_check_res
        if tp999_check_point is not None:
            self.tp999_check_point = tp999_check_point
        if tp999_check_res is not None:
            self.tp999_check_res = tp999_check_res
        if tp99_check_point is not None:
            self.tp99_check_point = tp99_check_point
        if tp99_check_res is not None:
            self.tp99_check_res = tp99_check_res
        if tps is not None:
            self.tps = tps
        if tps_check_point is not None:
            self.tps_check_point = tps_check_point
        if tps_check_res is not None:
            self.tps_check_res = tps_check_res
        if tran_tps is not None:
            self.tran_tps = tran_tps
        if tran_tps_check_point is not None:
            self.tran_tps_check_point = tran_tps_check_point
        if tran_tps_check_res is not None:
            self.tran_tps_check_res = tran_tps_check_res
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if transaction_success is not None:
            self.transaction_success = transaction_success
        if transactions is not None:
            self.transactions = transactions
        if transactions_check_point is not None:
            self.transactions_check_point = transactions_check_point
        if transactions_check_res is not None:
            self.transactions_check_res = transactions_check_res
        if update_time is not None:
            self.update_time = update_time
        if url is not None:
            self.url = url
        if user_concur is not None:
            self.user_concur = user_concur
        if version_uri is not None:
            self.version_uri = version_uri

    @property
    def max_success_rate_check_point(self):
        """Gets the max_success_rate_check_point of this CaseReportDetail.

        最大成功率检查点

        :return: The max_success_rate_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._max_success_rate_check_point

    @max_success_rate_check_point.setter
    def max_success_rate_check_point(self, max_success_rate_check_point):
        """Sets the max_success_rate_check_point of this CaseReportDetail.

        最大成功率检查点

        :param max_success_rate_check_point: The max_success_rate_check_point of this CaseReportDetail.
        :type max_success_rate_check_point: float
        """
        self._max_success_rate_check_point = max_success_rate_check_point

    @property
    def alias(self):
        """Gets the alias of this CaseReportDetail.

        别名

        :return: The alias of this CaseReportDetail.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this CaseReportDetail.

        别名

        :param alias: The alias of this CaseReportDetail.
        :type alias: str
        """
        self._alias = alias

    @property
    def average_resp_time(self):
        """Gets the average_resp_time of this CaseReportDetail.

        平均响应时间

        :return: The average_resp_time of this CaseReportDetail.
        :rtype: float
        """
        return self._average_resp_time

    @average_resp_time.setter
    def average_resp_time(self, average_resp_time):
        """Sets the average_resp_time of this CaseReportDetail.

        平均响应时间

        :param average_resp_time: The average_resp_time of this CaseReportDetail.
        :type average_resp_time: float
        """
        self._average_resp_time = average_resp_time

    @property
    def average_resp_time_check_point(self):
        """Gets the average_resp_time_check_point of this CaseReportDetail.

        平均响应时间检查点

        :return: The average_resp_time_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._average_resp_time_check_point

    @average_resp_time_check_point.setter
    def average_resp_time_check_point(self, average_resp_time_check_point):
        """Sets the average_resp_time_check_point of this CaseReportDetail.

        平均响应时间检查点

        :param average_resp_time_check_point: The average_resp_time_check_point of this CaseReportDetail.
        :type average_resp_time_check_point: float
        """
        self._average_resp_time_check_point = average_resp_time_check_point

    @property
    def average_resp_time_check_res(self):
        """Gets the average_resp_time_check_res of this CaseReportDetail.

        平均响应时间检查结果

        :return: The average_resp_time_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._average_resp_time_check_res

    @average_resp_time_check_res.setter
    def average_resp_time_check_res(self, average_resp_time_check_res):
        """Sets the average_resp_time_check_res of this CaseReportDetail.

        平均响应时间检查结果

        :param average_resp_time_check_res: The average_resp_time_check_res of this CaseReportDetail.
        :type average_resp_time_check_res: bool
        """
        self._average_resp_time_check_res = average_resp_time_check_res

    @property
    def avg_network_traffic(self):
        """Gets the avg_network_traffic of this CaseReportDetail.

        平均带宽

        :return: The avg_network_traffic of this CaseReportDetail.
        :rtype: float
        """
        return self._avg_network_traffic

    @avg_network_traffic.setter
    def avg_network_traffic(self, avg_network_traffic):
        """Sets the avg_network_traffic of this CaseReportDetail.

        平均带宽

        :param avg_network_traffic: The avg_network_traffic of this CaseReportDetail.
        :type avg_network_traffic: float
        """
        self._avg_network_traffic = avg_network_traffic

    @property
    def avg_rec_bytes(self):
        """Gets the avg_rec_bytes of this CaseReportDetail.

        平均下行带宽

        :return: The avg_rec_bytes of this CaseReportDetail.
        :rtype: int
        """
        return self._avg_rec_bytes

    @avg_rec_bytes.setter
    def avg_rec_bytes(self, avg_rec_bytes):
        """Sets the avg_rec_bytes of this CaseReportDetail.

        平均下行带宽

        :param avg_rec_bytes: The avg_rec_bytes of this CaseReportDetail.
        :type avg_rec_bytes: int
        """
        self._avg_rec_bytes = avg_rec_bytes

    @property
    def avg_rec_bytes_check_point(self):
        """Gets the avg_rec_bytes_check_point of this CaseReportDetail.

        平均下行带宽检查点

        :return: The avg_rec_bytes_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._avg_rec_bytes_check_point

    @avg_rec_bytes_check_point.setter
    def avg_rec_bytes_check_point(self, avg_rec_bytes_check_point):
        """Sets the avg_rec_bytes_check_point of this CaseReportDetail.

        平均下行带宽检查点

        :param avg_rec_bytes_check_point: The avg_rec_bytes_check_point of this CaseReportDetail.
        :type avg_rec_bytes_check_point: float
        """
        self._avg_rec_bytes_check_point = avg_rec_bytes_check_point

    @property
    def avg_rec_bytes_check_res(self):
        """Gets the avg_rec_bytes_check_res of this CaseReportDetail.

        平均下行带宽检查结果

        :return: The avg_rec_bytes_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._avg_rec_bytes_check_res

    @avg_rec_bytes_check_res.setter
    def avg_rec_bytes_check_res(self, avg_rec_bytes_check_res):
        """Sets the avg_rec_bytes_check_res of this CaseReportDetail.

        平均下行带宽检查结果

        :param avg_rec_bytes_check_res: The avg_rec_bytes_check_res of this CaseReportDetail.
        :type avg_rec_bytes_check_res: bool
        """
        self._avg_rec_bytes_check_res = avg_rec_bytes_check_res

    @property
    def avg_sent_bytes(self):
        """Gets the avg_sent_bytes of this CaseReportDetail.

        平均上行带宽

        :return: The avg_sent_bytes of this CaseReportDetail.
        :rtype: int
        """
        return self._avg_sent_bytes

    @avg_sent_bytes.setter
    def avg_sent_bytes(self, avg_sent_bytes):
        """Sets the avg_sent_bytes of this CaseReportDetail.

        平均上行带宽

        :param avg_sent_bytes: The avg_sent_bytes of this CaseReportDetail.
        :type avg_sent_bytes: int
        """
        self._avg_sent_bytes = avg_sent_bytes

    @property
    def avg_sent_bytes_check_point(self):
        """Gets the avg_sent_bytes_check_point of this CaseReportDetail.

        平均上行带宽检查点

        :return: The avg_sent_bytes_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._avg_sent_bytes_check_point

    @avg_sent_bytes_check_point.setter
    def avg_sent_bytes_check_point(self, avg_sent_bytes_check_point):
        """Sets the avg_sent_bytes_check_point of this CaseReportDetail.

        平均上行带宽检查点

        :param avg_sent_bytes_check_point: The avg_sent_bytes_check_point of this CaseReportDetail.
        :type avg_sent_bytes_check_point: float
        """
        self._avg_sent_bytes_check_point = avg_sent_bytes_check_point

    @property
    def avg_sent_bytes_check_res(self):
        """Gets the avg_sent_bytes_check_res of this CaseReportDetail.

        平均上行带宽检查结果

        :return: The avg_sent_bytes_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._avg_sent_bytes_check_res

    @avg_sent_bytes_check_res.setter
    def avg_sent_bytes_check_res(self, avg_sent_bytes_check_res):
        """Sets the avg_sent_bytes_check_res of this CaseReportDetail.

        平均上行带宽检查结果

        :param avg_sent_bytes_check_res: The avg_sent_bytes_check_res of this CaseReportDetail.
        :type avg_sent_bytes_check_res: bool
        """
        self._avg_sent_bytes_check_res = avg_sent_bytes_check_res

    @property
    def avg_tran_resp_time(self):
        """Gets the avg_tran_resp_time of this CaseReportDetail.

        事务平均响应时间

        :return: The avg_tran_resp_time of this CaseReportDetail.
        :rtype: float
        """
        return self._avg_tran_resp_time

    @avg_tran_resp_time.setter
    def avg_tran_resp_time(self, avg_tran_resp_time):
        """Sets the avg_tran_resp_time of this CaseReportDetail.

        事务平均响应时间

        :param avg_tran_resp_time: The avg_tran_resp_time of this CaseReportDetail.
        :type avg_tran_resp_time: float
        """
        self._avg_tran_resp_time = avg_tran_resp_time

    @property
    def avg_tran_resp_time_check_point(self):
        """Gets the avg_tran_resp_time_check_point of this CaseReportDetail.

        事务平均响应时间检查点

        :return: The avg_tran_resp_time_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._avg_tran_resp_time_check_point

    @avg_tran_resp_time_check_point.setter
    def avg_tran_resp_time_check_point(self, avg_tran_resp_time_check_point):
        """Sets the avg_tran_resp_time_check_point of this CaseReportDetail.

        事务平均响应时间检查点

        :param avg_tran_resp_time_check_point: The avg_tran_resp_time_check_point of this CaseReportDetail.
        :type avg_tran_resp_time_check_point: float
        """
        self._avg_tran_resp_time_check_point = avg_tran_resp_time_check_point

    @property
    def avg_tran_resp_time_check_res(self):
        """Gets the avg_tran_resp_time_check_res of this CaseReportDetail.

        事务平均响应时间检查结果

        :return: The avg_tran_resp_time_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._avg_tran_resp_time_check_res

    @avg_tran_resp_time_check_res.setter
    def avg_tran_resp_time_check_res(self, avg_tran_resp_time_check_res):
        """Sets the avg_tran_resp_time_check_res of this CaseReportDetail.

        事务平均响应时间检查结果

        :param avg_tran_resp_time_check_res: The avg_tran_resp_time_check_res of this CaseReportDetail.
        :type avg_tran_resp_time_check_res: bool
        """
        self._avg_tran_resp_time_check_res = avg_tran_resp_time_check_res

    @property
    def aw_id(self):
        """Gets the aw_id of this CaseReportDetail.

        awId

        :return: The aw_id of this CaseReportDetail.
        :rtype: str
        """
        return self._aw_id

    @aw_id.setter
    def aw_id(self, aw_id):
        """Sets the aw_id of this CaseReportDetail.

        awId

        :param aw_id: The aw_id of this CaseReportDetail.
        :type aw_id: str
        """
        self._aw_id = aw_id

    @property
    def case_uri(self):
        """Gets the case_uri of this CaseReportDetail.

        用例Uri

        :return: The case_uri of this CaseReportDetail.
        :rtype: str
        """
        return self._case_uri

    @case_uri.setter
    def case_uri(self, case_uri):
        """Sets the case_uri of this CaseReportDetail.

        用例Uri

        :param case_uri: The case_uri of this CaseReportDetail.
        :type case_uri: str
        """
        self._case_uri = case_uri

    @property
    def checkpoint_result(self):
        """Gets the checkpoint_result of this CaseReportDetail.

        所有检查点结果的汇总结果

        :return: The checkpoint_result of this CaseReportDetail.
        :rtype: bool
        """
        return self._checkpoint_result

    @checkpoint_result.setter
    def checkpoint_result(self, checkpoint_result):
        """Sets the checkpoint_result of this CaseReportDetail.

        所有检查点结果的汇总结果

        :param checkpoint_result: The checkpoint_result of this CaseReportDetail.
        :type checkpoint_result: bool
        """
        self._checkpoint_result = checkpoint_result

    @property
    def cpu_usage(self):
        """Gets the cpu_usage of this CaseReportDetail.

        cpu最大使用率

        :return: The cpu_usage of this CaseReportDetail.
        :rtype: float
        """
        return self._cpu_usage

    @cpu_usage.setter
    def cpu_usage(self, cpu_usage):
        """Sets the cpu_usage of this CaseReportDetail.

        cpu最大使用率

        :param cpu_usage: The cpu_usage of this CaseReportDetail.
        :type cpu_usage: float
        """
        self._cpu_usage = cpu_usage

    @property
    def cpu_usage_avg(self):
        """Gets the cpu_usage_avg of this CaseReportDetail.

        cpu平均使用率

        :return: The cpu_usage_avg of this CaseReportDetail.
        :rtype: float
        """
        return self._cpu_usage_avg

    @cpu_usage_avg.setter
    def cpu_usage_avg(self, cpu_usage_avg):
        """Sets the cpu_usage_avg of this CaseReportDetail.

        cpu平均使用率

        :param cpu_usage_avg: The cpu_usage_avg of this CaseReportDetail.
        :type cpu_usage_avg: float
        """
        self._cpu_usage_avg = cpu_usage_avg

    @property
    def cpu_usage_avg_check_point(self):
        """Gets the cpu_usage_avg_check_point of this CaseReportDetail.

        cpu平均使用率检查点

        :return: The cpu_usage_avg_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._cpu_usage_avg_check_point

    @cpu_usage_avg_check_point.setter
    def cpu_usage_avg_check_point(self, cpu_usage_avg_check_point):
        """Sets the cpu_usage_avg_check_point of this CaseReportDetail.

        cpu平均使用率检查点

        :param cpu_usage_avg_check_point: The cpu_usage_avg_check_point of this CaseReportDetail.
        :type cpu_usage_avg_check_point: float
        """
        self._cpu_usage_avg_check_point = cpu_usage_avg_check_point

    @property
    def cpu_usage_avg_check_res(self):
        """Gets the cpu_usage_avg_check_res of this CaseReportDetail.

        cpu平均使用率检查结果

        :return: The cpu_usage_avg_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._cpu_usage_avg_check_res

    @cpu_usage_avg_check_res.setter
    def cpu_usage_avg_check_res(self, cpu_usage_avg_check_res):
        """Sets the cpu_usage_avg_check_res of this CaseReportDetail.

        cpu平均使用率检查结果

        :param cpu_usage_avg_check_res: The cpu_usage_avg_check_res of this CaseReportDetail.
        :type cpu_usage_avg_check_res: bool
        """
        self._cpu_usage_avg_check_res = cpu_usage_avg_check_res

    @property
    def cpu_usage_check_point(self):
        """Gets the cpu_usage_check_point of this CaseReportDetail.

        cpu最大使用率检查点

        :return: The cpu_usage_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._cpu_usage_check_point

    @cpu_usage_check_point.setter
    def cpu_usage_check_point(self, cpu_usage_check_point):
        """Sets the cpu_usage_check_point of this CaseReportDetail.

        cpu最大使用率检查点

        :param cpu_usage_check_point: The cpu_usage_check_point of this CaseReportDetail.
        :type cpu_usage_check_point: float
        """
        self._cpu_usage_check_point = cpu_usage_check_point

    @property
    def cpu_usage_check_res(self):
        """Gets the cpu_usage_check_res of this CaseReportDetail.

        cpu最大使用率检查结果

        :return: The cpu_usage_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._cpu_usage_check_res

    @cpu_usage_check_res.setter
    def cpu_usage_check_res(self, cpu_usage_check_res):
        """Sets the cpu_usage_check_res of this CaseReportDetail.

        cpu最大使用率检查结果

        :param cpu_usage_check_res: The cpu_usage_check_res of this CaseReportDetail.
        :type cpu_usage_check_res: bool
        """
        self._cpu_usage_check_res = cpu_usage_check_res

    @property
    def create_time(self):
        """Gets the create_time of this CaseReportDetail.

        创建时间

        :return: The create_time of this CaseReportDetail.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CaseReportDetail.

        创建时间

        :param create_time: The create_time of this CaseReportDetail.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def current_thread_num(self):
        """Gets the current_thread_num of this CaseReportDetail.

        最大并发数

        :return: The current_thread_num of this CaseReportDetail.
        :rtype: int
        """
        return self._current_thread_num

    @current_thread_num.setter
    def current_thread_num(self, current_thread_num):
        """Sets the current_thread_num of this CaseReportDetail.

        最大并发数

        :param current_thread_num: The current_thread_num of this CaseReportDetail.
        :type current_thread_num: int
        """
        self._current_thread_num = current_thread_num

    @property
    def datum_type(self):
        """Gets the datum_type of this CaseReportDetail.

        数据类型(case/aw/transaction)

        :return: The datum_type of this CaseReportDetail.
        :rtype: int
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type):
        """Sets the datum_type of this CaseReportDetail.

        数据类型(case/aw/transaction)

        :param datum_type: The datum_type of this CaseReportDetail.
        :type datum_type: int
        """
        self._datum_type = datum_type

    @property
    def dcs_latency_avg(self):
        """Gets the dcs_latency_avg of this CaseReportDetail.

        dcs平均时延

        :return: The dcs_latency_avg of this CaseReportDetail.
        :rtype: float
        """
        return self._dcs_latency_avg

    @dcs_latency_avg.setter
    def dcs_latency_avg(self, dcs_latency_avg):
        """Sets the dcs_latency_avg of this CaseReportDetail.

        dcs平均时延

        :param dcs_latency_avg: The dcs_latency_avg of this CaseReportDetail.
        :type dcs_latency_avg: float
        """
        self._dcs_latency_avg = dcs_latency_avg

    @property
    def dcs_latency_avg_check_point(self):
        """Gets the dcs_latency_avg_check_point of this CaseReportDetail.

        dcs平均时延检查点

        :return: The dcs_latency_avg_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._dcs_latency_avg_check_point

    @dcs_latency_avg_check_point.setter
    def dcs_latency_avg_check_point(self, dcs_latency_avg_check_point):
        """Sets the dcs_latency_avg_check_point of this CaseReportDetail.

        dcs平均时延检查点

        :param dcs_latency_avg_check_point: The dcs_latency_avg_check_point of this CaseReportDetail.
        :type dcs_latency_avg_check_point: float
        """
        self._dcs_latency_avg_check_point = dcs_latency_avg_check_point

    @property
    def dcs_latency_avg_check_res(self):
        """Gets the dcs_latency_avg_check_res of this CaseReportDetail.

        dcs平均时延检查结果

        :return: The dcs_latency_avg_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._dcs_latency_avg_check_res

    @dcs_latency_avg_check_res.setter
    def dcs_latency_avg_check_res(self, dcs_latency_avg_check_res):
        """Sets the dcs_latency_avg_check_res of this CaseReportDetail.

        dcs平均时延检查结果

        :param dcs_latency_avg_check_res: The dcs_latency_avg_check_res of this CaseReportDetail.
        :type dcs_latency_avg_check_res: bool
        """
        self._dcs_latency_avg_check_res = dcs_latency_avg_check_res

    @property
    def dcs_latency_max(self):
        """Gets the dcs_latency_max of this CaseReportDetail.

        dcs最大时延

        :return: The dcs_latency_max of this CaseReportDetail.
        :rtype: float
        """
        return self._dcs_latency_max

    @dcs_latency_max.setter
    def dcs_latency_max(self, dcs_latency_max):
        """Sets the dcs_latency_max of this CaseReportDetail.

        dcs最大时延

        :param dcs_latency_max: The dcs_latency_max of this CaseReportDetail.
        :type dcs_latency_max: float
        """
        self._dcs_latency_max = dcs_latency_max

    @property
    def dcs_latency_max_check_point(self):
        """Gets the dcs_latency_max_check_point of this CaseReportDetail.

        dcs最大时延检查点·

        :return: The dcs_latency_max_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._dcs_latency_max_check_point

    @dcs_latency_max_check_point.setter
    def dcs_latency_max_check_point(self, dcs_latency_max_check_point):
        """Sets the dcs_latency_max_check_point of this CaseReportDetail.

        dcs最大时延检查点·

        :param dcs_latency_max_check_point: The dcs_latency_max_check_point of this CaseReportDetail.
        :type dcs_latency_max_check_point: float
        """
        self._dcs_latency_max_check_point = dcs_latency_max_check_point

    @property
    def dcs_latency_max_check_res(self):
        """Gets the dcs_latency_max_check_res of this CaseReportDetail.

        dcs最大时延检查结果

        :return: The dcs_latency_max_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._dcs_latency_max_check_res

    @dcs_latency_max_check_res.setter
    def dcs_latency_max_check_res(self, dcs_latency_max_check_res):
        """Sets the dcs_latency_max_check_res of this CaseReportDetail.

        dcs最大时延检查结果

        :param dcs_latency_max_check_res: The dcs_latency_max_check_res of this CaseReportDetail.
        :type dcs_latency_max_check_res: bool
        """
        self._dcs_latency_max_check_res = dcs_latency_max_check_res

    @property
    def dcs_latency_min(self):
        """Gets the dcs_latency_min of this CaseReportDetail.

        dcs最小时延

        :return: The dcs_latency_min of this CaseReportDetail.
        :rtype: float
        """
        return self._dcs_latency_min

    @dcs_latency_min.setter
    def dcs_latency_min(self, dcs_latency_min):
        """Sets the dcs_latency_min of this CaseReportDetail.

        dcs最小时延

        :param dcs_latency_min: The dcs_latency_min of this CaseReportDetail.
        :type dcs_latency_min: float
        """
        self._dcs_latency_min = dcs_latency_min

    @property
    def dcs_latency_min_check_point(self):
        """Gets the dcs_latency_min_check_point of this CaseReportDetail.

        dcs最小时延检查点

        :return: The dcs_latency_min_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._dcs_latency_min_check_point

    @dcs_latency_min_check_point.setter
    def dcs_latency_min_check_point(self, dcs_latency_min_check_point):
        """Sets the dcs_latency_min_check_point of this CaseReportDetail.

        dcs最小时延检查点

        :param dcs_latency_min_check_point: The dcs_latency_min_check_point of this CaseReportDetail.
        :type dcs_latency_min_check_point: float
        """
        self._dcs_latency_min_check_point = dcs_latency_min_check_point

    @property
    def dcs_latency_min_check_res(self):
        """Gets the dcs_latency_min_check_res of this CaseReportDetail.

        dcs最小时延检查结果

        :return: The dcs_latency_min_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._dcs_latency_min_check_res

    @dcs_latency_min_check_res.setter
    def dcs_latency_min_check_res(self, dcs_latency_min_check_res):
        """Sets the dcs_latency_min_check_res of this CaseReportDetail.

        dcs最小时延检查结果

        :param dcs_latency_min_check_res: The dcs_latency_min_check_res of this CaseReportDetail.
        :type dcs_latency_min_check_res: bool
        """
        self._dcs_latency_min_check_res = dcs_latency_min_check_res

    @property
    def detail_id(self):
        """Gets the detail_id of this CaseReportDetail.

        用例/aw/事务在数据库中dc_case_aw表的主键ID

        :return: The detail_id of this CaseReportDetail.
        :rtype: str
        """
        return self._detail_id

    @detail_id.setter
    def detail_id(self, detail_id):
        """Sets the detail_id of this CaseReportDetail.

        用例/aw/事务在数据库中dc_case_aw表的主键ID

        :param detail_id: The detail_id of this CaseReportDetail.
        :type detail_id: str
        """
        self._detail_id = detail_id

    @property
    def disk_read(self):
        """Gets the disk_read of this CaseReportDetail.

        磁盘最大读取速度

        :return: The disk_read of this CaseReportDetail.
        :rtype: float
        """
        return self._disk_read

    @disk_read.setter
    def disk_read(self, disk_read):
        """Sets the disk_read of this CaseReportDetail.

        磁盘最大读取速度

        :param disk_read: The disk_read of this CaseReportDetail.
        :type disk_read: float
        """
        self._disk_read = disk_read

    @property
    def disk_read_avg(self):
        """Gets the disk_read_avg of this CaseReportDetail.

        磁盘平均读取速度

        :return: The disk_read_avg of this CaseReportDetail.
        :rtype: float
        """
        return self._disk_read_avg

    @disk_read_avg.setter
    def disk_read_avg(self, disk_read_avg):
        """Sets the disk_read_avg of this CaseReportDetail.

        磁盘平均读取速度

        :param disk_read_avg: The disk_read_avg of this CaseReportDetail.
        :type disk_read_avg: float
        """
        self._disk_read_avg = disk_read_avg

    @property
    def disk_read_avg_check_point(self):
        """Gets the disk_read_avg_check_point of this CaseReportDetail.

        磁盘平均读取速度检查点

        :return: The disk_read_avg_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._disk_read_avg_check_point

    @disk_read_avg_check_point.setter
    def disk_read_avg_check_point(self, disk_read_avg_check_point):
        """Sets the disk_read_avg_check_point of this CaseReportDetail.

        磁盘平均读取速度检查点

        :param disk_read_avg_check_point: The disk_read_avg_check_point of this CaseReportDetail.
        :type disk_read_avg_check_point: float
        """
        self._disk_read_avg_check_point = disk_read_avg_check_point

    @property
    def disk_read_avg_check_res(self):
        """Gets the disk_read_avg_check_res of this CaseReportDetail.

        磁盘平均读取速度检查结果

        :return: The disk_read_avg_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._disk_read_avg_check_res

    @disk_read_avg_check_res.setter
    def disk_read_avg_check_res(self, disk_read_avg_check_res):
        """Sets the disk_read_avg_check_res of this CaseReportDetail.

        磁盘平均读取速度检查结果

        :param disk_read_avg_check_res: The disk_read_avg_check_res of this CaseReportDetail.
        :type disk_read_avg_check_res: bool
        """
        self._disk_read_avg_check_res = disk_read_avg_check_res

    @property
    def disk_read_check_point(self):
        """Gets the disk_read_check_point of this CaseReportDetail.

        磁盘最大读取速度检查点

        :return: The disk_read_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._disk_read_check_point

    @disk_read_check_point.setter
    def disk_read_check_point(self, disk_read_check_point):
        """Sets the disk_read_check_point of this CaseReportDetail.

        磁盘最大读取速度检查点

        :param disk_read_check_point: The disk_read_check_point of this CaseReportDetail.
        :type disk_read_check_point: float
        """
        self._disk_read_check_point = disk_read_check_point

    @property
    def disk_read_check_res(self):
        """Gets the disk_read_check_res of this CaseReportDetail.

        磁盘最大读取速度检查结果

        :return: The disk_read_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._disk_read_check_res

    @disk_read_check_res.setter
    def disk_read_check_res(self, disk_read_check_res):
        """Sets the disk_read_check_res of this CaseReportDetail.

        磁盘最大读取速度检查结果

        :param disk_read_check_res: The disk_read_check_res of this CaseReportDetail.
        :type disk_read_check_res: bool
        """
        self._disk_read_check_res = disk_read_check_res

    @property
    def disk_usage(self):
        """Gets the disk_usage of this CaseReportDetail.

        磁盘最大使用率

        :return: The disk_usage of this CaseReportDetail.
        :rtype: float
        """
        return self._disk_usage

    @disk_usage.setter
    def disk_usage(self, disk_usage):
        """Sets the disk_usage of this CaseReportDetail.

        磁盘最大使用率

        :param disk_usage: The disk_usage of this CaseReportDetail.
        :type disk_usage: float
        """
        self._disk_usage = disk_usage

    @property
    def disk_usage_avg(self):
        """Gets the disk_usage_avg of this CaseReportDetail.

        磁盘平均使用率

        :return: The disk_usage_avg of this CaseReportDetail.
        :rtype: float
        """
        return self._disk_usage_avg

    @disk_usage_avg.setter
    def disk_usage_avg(self, disk_usage_avg):
        """Sets the disk_usage_avg of this CaseReportDetail.

        磁盘平均使用率

        :param disk_usage_avg: The disk_usage_avg of this CaseReportDetail.
        :type disk_usage_avg: float
        """
        self._disk_usage_avg = disk_usage_avg

    @property
    def disk_usage_avg_check_point(self):
        """Gets the disk_usage_avg_check_point of this CaseReportDetail.

        磁盘平均使用率检查点

        :return: The disk_usage_avg_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._disk_usage_avg_check_point

    @disk_usage_avg_check_point.setter
    def disk_usage_avg_check_point(self, disk_usage_avg_check_point):
        """Sets the disk_usage_avg_check_point of this CaseReportDetail.

        磁盘平均使用率检查点

        :param disk_usage_avg_check_point: The disk_usage_avg_check_point of this CaseReportDetail.
        :type disk_usage_avg_check_point: float
        """
        self._disk_usage_avg_check_point = disk_usage_avg_check_point

    @property
    def disk_usage_avg_check_res(self):
        """Gets the disk_usage_avg_check_res of this CaseReportDetail.

        磁盘平均使用率检查结果

        :return: The disk_usage_avg_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._disk_usage_avg_check_res

    @disk_usage_avg_check_res.setter
    def disk_usage_avg_check_res(self, disk_usage_avg_check_res):
        """Sets the disk_usage_avg_check_res of this CaseReportDetail.

        磁盘平均使用率检查结果

        :param disk_usage_avg_check_res: The disk_usage_avg_check_res of this CaseReportDetail.
        :type disk_usage_avg_check_res: bool
        """
        self._disk_usage_avg_check_res = disk_usage_avg_check_res

    @property
    def disk_usage_check_point(self):
        """Gets the disk_usage_check_point of this CaseReportDetail.

        磁盘最大使用率检查点

        :return: The disk_usage_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._disk_usage_check_point

    @disk_usage_check_point.setter
    def disk_usage_check_point(self, disk_usage_check_point):
        """Sets the disk_usage_check_point of this CaseReportDetail.

        磁盘最大使用率检查点

        :param disk_usage_check_point: The disk_usage_check_point of this CaseReportDetail.
        :type disk_usage_check_point: float
        """
        self._disk_usage_check_point = disk_usage_check_point

    @property
    def disk_usage_check_res(self):
        """Gets the disk_usage_check_res of this CaseReportDetail.

        磁盘最大使用率检查结果

        :return: The disk_usage_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._disk_usage_check_res

    @disk_usage_check_res.setter
    def disk_usage_check_res(self, disk_usage_check_res):
        """Sets the disk_usage_check_res of this CaseReportDetail.

        磁盘最大使用率检查结果

        :param disk_usage_check_res: The disk_usage_check_res of this CaseReportDetail.
        :type disk_usage_check_res: bool
        """
        self._disk_usage_check_res = disk_usage_check_res

    @property
    def disk_write(self):
        """Gets the disk_write of this CaseReportDetail.

        磁盘最大写入速度

        :return: The disk_write of this CaseReportDetail.
        :rtype: float
        """
        return self._disk_write

    @disk_write.setter
    def disk_write(self, disk_write):
        """Sets the disk_write of this CaseReportDetail.

        磁盘最大写入速度

        :param disk_write: The disk_write of this CaseReportDetail.
        :type disk_write: float
        """
        self._disk_write = disk_write

    @property
    def disk_write_avg(self):
        """Gets the disk_write_avg of this CaseReportDetail.

        磁盘平均写入速度

        :return: The disk_write_avg of this CaseReportDetail.
        :rtype: float
        """
        return self._disk_write_avg

    @disk_write_avg.setter
    def disk_write_avg(self, disk_write_avg):
        """Sets the disk_write_avg of this CaseReportDetail.

        磁盘平均写入速度

        :param disk_write_avg: The disk_write_avg of this CaseReportDetail.
        :type disk_write_avg: float
        """
        self._disk_write_avg = disk_write_avg

    @property
    def disk_write_avg_check_point(self):
        """Gets the disk_write_avg_check_point of this CaseReportDetail.

        磁盘平均写入速度检查点

        :return: The disk_write_avg_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._disk_write_avg_check_point

    @disk_write_avg_check_point.setter
    def disk_write_avg_check_point(self, disk_write_avg_check_point):
        """Sets the disk_write_avg_check_point of this CaseReportDetail.

        磁盘平均写入速度检查点

        :param disk_write_avg_check_point: The disk_write_avg_check_point of this CaseReportDetail.
        :type disk_write_avg_check_point: float
        """
        self._disk_write_avg_check_point = disk_write_avg_check_point

    @property
    def disk_write_avg_check_res(self):
        """Gets the disk_write_avg_check_res of this CaseReportDetail.

        磁盘平均写入速度检查结果

        :return: The disk_write_avg_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._disk_write_avg_check_res

    @disk_write_avg_check_res.setter
    def disk_write_avg_check_res(self, disk_write_avg_check_res):
        """Sets the disk_write_avg_check_res of this CaseReportDetail.

        磁盘平均写入速度检查结果

        :param disk_write_avg_check_res: The disk_write_avg_check_res of this CaseReportDetail.
        :type disk_write_avg_check_res: bool
        """
        self._disk_write_avg_check_res = disk_write_avg_check_res

    @property
    def disk_write_check_point(self):
        """Gets the disk_write_check_point of this CaseReportDetail.

        磁盘最大写入速度检查点

        :return: The disk_write_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._disk_write_check_point

    @disk_write_check_point.setter
    def disk_write_check_point(self, disk_write_check_point):
        """Sets the disk_write_check_point of this CaseReportDetail.

        磁盘最大写入速度检查点

        :param disk_write_check_point: The disk_write_check_point of this CaseReportDetail.
        :type disk_write_check_point: float
        """
        self._disk_write_check_point = disk_write_check_point

    @property
    def disk_write_check_res(self):
        """Gets the disk_write_check_res of this CaseReportDetail.

        磁盘最大写入速度检查结果

        :return: The disk_write_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._disk_write_check_res

    @disk_write_check_res.setter
    def disk_write_check_res(self, disk_write_check_res):
        """Sets the disk_write_check_res of this CaseReportDetail.

        磁盘最大写入速度检查结果

        :param disk_write_check_res: The disk_write_check_res of this CaseReportDetail.
        :type disk_write_check_res: bool
        """
        self._disk_write_check_res = disk_write_check_res

    @property
    def duration(self):
        """Gets the duration of this CaseReportDetail.

        运行时长

        :return: The duration of this CaseReportDetail.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this CaseReportDetail.

        运行时长

        :param duration: The duration of this CaseReportDetail.
        :type duration: int
        """
        self._duration = duration

    @property
    def end_time(self):
        """Gets the end_time of this CaseReportDetail.

        结束时间

        :return: The end_time of this CaseReportDetail.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CaseReportDetail.

        结束时间

        :param end_time: The end_time of this CaseReportDetail.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def error_count(self):
        """Gets the error_count of this CaseReportDetail.

        错误数

        :return: The error_count of this CaseReportDetail.
        :rtype: int
        """
        return self._error_count

    @error_count.setter
    def error_count(self, error_count):
        """Sets the error_count of this CaseReportDetail.

        错误数

        :param error_count: The error_count of this CaseReportDetail.
        :type error_count: int
        """
        self._error_count = error_count

    @property
    def error_events_count(self):
        """Gets the error_events_count of this CaseReportDetail.

        错误事件数

        :return: The error_events_count of this CaseReportDetail.
        :rtype: int
        """
        return self._error_events_count

    @error_events_count.setter
    def error_events_count(self, error_events_count):
        """Sets the error_events_count of this CaseReportDetail.

        错误事件数

        :param error_events_count: The error_events_count of this CaseReportDetail.
        :type error_events_count: int
        """
        self._error_events_count = error_events_count

    @property
    def failed_assert(self):
        """Gets the failed_assert of this CaseReportDetail.

        断言失败数

        :return: The failed_assert of this CaseReportDetail.
        :rtype: int
        """
        return self._failed_assert

    @failed_assert.setter
    def failed_assert(self, failed_assert):
        """Sets the failed_assert of this CaseReportDetail.

        断言失败数

        :param failed_assert: The failed_assert of this CaseReportDetail.
        :type failed_assert: int
        """
        self._failed_assert = failed_assert

    @property
    def failed_others(self):
        """Gets the failed_others of this CaseReportDetail.

        其他失败数

        :return: The failed_others of this CaseReportDetail.
        :rtype: int
        """
        return self._failed_others

    @failed_others.setter
    def failed_others(self, failed_others):
        """Sets the failed_others of this CaseReportDetail.

        其他失败数

        :param failed_others: The failed_others of this CaseReportDetail.
        :type failed_others: int
        """
        self._failed_others = failed_others

    @property
    def failed_parsed(self):
        """Gets the failed_parsed of this CaseReportDetail.

        解析失败数

        :return: The failed_parsed of this CaseReportDetail.
        :rtype: int
        """
        return self._failed_parsed

    @failed_parsed.setter
    def failed_parsed(self, failed_parsed):
        """Sets the failed_parsed of this CaseReportDetail.

        解析失败数

        :param failed_parsed: The failed_parsed of this CaseReportDetail.
        :type failed_parsed: int
        """
        self._failed_parsed = failed_parsed

    @property
    def failed_reason(self):
        """Gets the failed_reason of this CaseReportDetail.

        失败原因

        :return: The failed_reason of this CaseReportDetail.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this CaseReportDetail.

        失败原因

        :param failed_reason: The failed_reason of this CaseReportDetail.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def failed_refused(self):
        """Gets the failed_refused of this CaseReportDetail.

        连接拒绝失败数

        :return: The failed_refused of this CaseReportDetail.
        :rtype: int
        """
        return self._failed_refused

    @failed_refused.setter
    def failed_refused(self, failed_refused):
        """Sets the failed_refused of this CaseReportDetail.

        连接拒绝失败数

        :param failed_refused: The failed_refused of this CaseReportDetail.
        :type failed_refused: int
        """
        self._failed_refused = failed_refused

    @property
    def failed_timeout(self):
        """Gets the failed_timeout of this CaseReportDetail.

        连接超时失败数

        :return: The failed_timeout of this CaseReportDetail.
        :rtype: int
        """
        return self._failed_timeout

    @failed_timeout.setter
    def failed_timeout(self, failed_timeout):
        """Sets the failed_timeout of this CaseReportDetail.

        连接超时失败数

        :param failed_timeout: The failed_timeout of this CaseReportDetail.
        :type failed_timeout: int
        """
        self._failed_timeout = failed_timeout

    @property
    def id(self):
        """Gets the id of this CaseReportDetail.

        用例在数据库中dc_testcase表的主键id

        :return: The id of this CaseReportDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CaseReportDetail.

        用例在数据库中dc_testcase表的主键id

        :param id: The id of this CaseReportDetail.
        :type id: str
        """
        self._id = id

    @property
    def is_aw(self):
        """Gets the is_aw of this CaseReportDetail.

        是否是aw

        :return: The is_aw of this CaseReportDetail.
        :rtype: bool
        """
        return self._is_aw

    @is_aw.setter
    def is_aw(self, is_aw):
        """Sets the is_aw of this CaseReportDetail.

        是否是aw

        :param is_aw: The is_aw of this CaseReportDetail.
        :type is_aw: bool
        """
        self._is_aw = is_aw

    @property
    def iteration_uri(self):
        """Gets the iteration_uri of this CaseReportDetail.

        迭代uri

        :return: The iteration_uri of this CaseReportDetail.
        :rtype: str
        """
        return self._iteration_uri

    @iteration_uri.setter
    def iteration_uri(self, iteration_uri):
        """Sets the iteration_uri of this CaseReportDetail.

        迭代uri

        :param iteration_uri: The iteration_uri of this CaseReportDetail.
        :type iteration_uri: str
        """
        self._iteration_uri = iteration_uri

    @property
    def kpi_monitor(self):
        """Gets the kpi_monitor of this CaseReportDetail.

        来源于设计服务的监控数据

        :return: The kpi_monitor of this CaseReportDetail.
        :rtype: str
        """
        return self._kpi_monitor

    @kpi_monitor.setter
    def kpi_monitor(self, kpi_monitor):
        """Sets the kpi_monitor of this CaseReportDetail.

        来源于设计服务的监控数据

        :param kpi_monitor: The kpi_monitor of this CaseReportDetail.
        :type kpi_monitor: str
        """
        self._kpi_monitor = kpi_monitor

    @property
    def max(self):
        """Gets the max of this CaseReportDetail.

        最大响应时间

        :return: The max of this CaseReportDetail.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this CaseReportDetail.

        最大响应时间

        :param max: The max of this CaseReportDetail.
        :type max: int
        """
        self._max = max

    @property
    def max_avg_time(self):
        """Gets the max_avg_time of this CaseReportDetail.

        平均响应时间

        :return: The max_avg_time of this CaseReportDetail.
        :rtype: float
        """
        return self._max_avg_time

    @max_avg_time.setter
    def max_avg_time(self, max_avg_time):
        """Sets the max_avg_time of this CaseReportDetail.

        平均响应时间

        :param max_avg_time: The max_avg_time of this CaseReportDetail.
        :type max_avg_time: float
        """
        self._max_avg_time = max_avg_time

    @property
    def max_avg_time_check_point(self):
        """Gets the max_avg_time_check_point of this CaseReportDetail.

        平均响应时间检查点

        :return: The max_avg_time_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._max_avg_time_check_point

    @max_avg_time_check_point.setter
    def max_avg_time_check_point(self, max_avg_time_check_point):
        """Sets the max_avg_time_check_point of this CaseReportDetail.

        平均响应时间检查点

        :param max_avg_time_check_point: The max_avg_time_check_point of this CaseReportDetail.
        :type max_avg_time_check_point: float
        """
        self._max_avg_time_check_point = max_avg_time_check_point

    @property
    def max_avg_time_check_res(self):
        """Gets the max_avg_time_check_res of this CaseReportDetail.

        平均响应时间检查结果

        :return: The max_avg_time_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._max_avg_time_check_res

    @max_avg_time_check_res.setter
    def max_avg_time_check_res(self, max_avg_time_check_res):
        """Sets the max_avg_time_check_res of this CaseReportDetail.

        平均响应时间检查结果

        :param max_avg_time_check_res: The max_avg_time_check_res of this CaseReportDetail.
        :type max_avg_time_check_res: bool
        """
        self._max_avg_time_check_res = max_avg_time_check_res

    @property
    def max_network_traffic(self):
        """Gets the max_network_traffic of this CaseReportDetail.

        流量峰值

        :return: The max_network_traffic of this CaseReportDetail.
        :rtype: int
        """
        return self._max_network_traffic

    @max_network_traffic.setter
    def max_network_traffic(self, max_network_traffic):
        """Sets the max_network_traffic of this CaseReportDetail.

        流量峰值

        :param max_network_traffic: The max_network_traffic of this CaseReportDetail.
        :type max_network_traffic: int
        """
        self._max_network_traffic = max_network_traffic

    @property
    def max_rec_bytes(self):
        """Gets the max_rec_bytes of this CaseReportDetail.

        最大下行带宽

        :return: The max_rec_bytes of this CaseReportDetail.
        :rtype: int
        """
        return self._max_rec_bytes

    @max_rec_bytes.setter
    def max_rec_bytes(self, max_rec_bytes):
        """Sets the max_rec_bytes of this CaseReportDetail.

        最大下行带宽

        :param max_rec_bytes: The max_rec_bytes of this CaseReportDetail.
        :type max_rec_bytes: int
        """
        self._max_rec_bytes = max_rec_bytes

    @property
    def max_rec_bytes_check_point(self):
        """Gets the max_rec_bytes_check_point of this CaseReportDetail.

        最大下行带宽检查点

        :return: The max_rec_bytes_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._max_rec_bytes_check_point

    @max_rec_bytes_check_point.setter
    def max_rec_bytes_check_point(self, max_rec_bytes_check_point):
        """Sets the max_rec_bytes_check_point of this CaseReportDetail.

        最大下行带宽检查点

        :param max_rec_bytes_check_point: The max_rec_bytes_check_point of this CaseReportDetail.
        :type max_rec_bytes_check_point: float
        """
        self._max_rec_bytes_check_point = max_rec_bytes_check_point

    @property
    def max_rec_bytes_check_res(self):
        """Gets the max_rec_bytes_check_res of this CaseReportDetail.

        最大下行带宽检查结果

        :return: The max_rec_bytes_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._max_rec_bytes_check_res

    @max_rec_bytes_check_res.setter
    def max_rec_bytes_check_res(self, max_rec_bytes_check_res):
        """Sets the max_rec_bytes_check_res of this CaseReportDetail.

        最大下行带宽检查结果

        :param max_rec_bytes_check_res: The max_rec_bytes_check_res of this CaseReportDetail.
        :type max_rec_bytes_check_res: bool
        """
        self._max_rec_bytes_check_res = max_rec_bytes_check_res

    @property
    def max_resp_time(self):
        """Gets the max_resp_time of this CaseReportDetail.

        最大响应时间

        :return: The max_resp_time of this CaseReportDetail.
        :rtype: int
        """
        return self._max_resp_time

    @max_resp_time.setter
    def max_resp_time(self, max_resp_time):
        """Sets the max_resp_time of this CaseReportDetail.

        最大响应时间

        :param max_resp_time: The max_resp_time of this CaseReportDetail.
        :type max_resp_time: int
        """
        self._max_resp_time = max_resp_time

    @property
    def max_resp_time_check_point(self):
        """Gets the max_resp_time_check_point of this CaseReportDetail.

        最大响应时间检查点

        :return: The max_resp_time_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._max_resp_time_check_point

    @max_resp_time_check_point.setter
    def max_resp_time_check_point(self, max_resp_time_check_point):
        """Sets the max_resp_time_check_point of this CaseReportDetail.

        最大响应时间检查点

        :param max_resp_time_check_point: The max_resp_time_check_point of this CaseReportDetail.
        :type max_resp_time_check_point: float
        """
        self._max_resp_time_check_point = max_resp_time_check_point

    @property
    def max_resp_time_check_res(self):
        """Gets the max_resp_time_check_res of this CaseReportDetail.

        最大响应时间检查结果

        :return: The max_resp_time_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._max_resp_time_check_res

    @max_resp_time_check_res.setter
    def max_resp_time_check_res(self, max_resp_time_check_res):
        """Sets the max_resp_time_check_res of this CaseReportDetail.

        最大响应时间检查结果

        :param max_resp_time_check_res: The max_resp_time_check_res of this CaseReportDetail.
        :type max_resp_time_check_res: bool
        """
        self._max_resp_time_check_res = max_resp_time_check_res

    @property
    def max_rps(self):
        """Gets the max_rps of this CaseReportDetail.

        最大RPS

        :return: The max_rps of this CaseReportDetail.
        :rtype: int
        """
        return self._max_rps

    @max_rps.setter
    def max_rps(self, max_rps):
        """Sets the max_rps of this CaseReportDetail.

        最大RPS

        :param max_rps: The max_rps of this CaseReportDetail.
        :type max_rps: int
        """
        self._max_rps = max_rps

    @property
    def max_sent_bytes(self):
        """Gets the max_sent_bytes of this CaseReportDetail.

        最大上行带宽

        :return: The max_sent_bytes of this CaseReportDetail.
        :rtype: int
        """
        return self._max_sent_bytes

    @max_sent_bytes.setter
    def max_sent_bytes(self, max_sent_bytes):
        """Sets the max_sent_bytes of this CaseReportDetail.

        最大上行带宽

        :param max_sent_bytes: The max_sent_bytes of this CaseReportDetail.
        :type max_sent_bytes: int
        """
        self._max_sent_bytes = max_sent_bytes

    @property
    def max_sent_bytes_check_point(self):
        """Gets the max_sent_bytes_check_point of this CaseReportDetail.

        最大上行带宽检查点

        :return: The max_sent_bytes_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._max_sent_bytes_check_point

    @max_sent_bytes_check_point.setter
    def max_sent_bytes_check_point(self, max_sent_bytes_check_point):
        """Sets the max_sent_bytes_check_point of this CaseReportDetail.

        最大上行带宽检查点

        :param max_sent_bytes_check_point: The max_sent_bytes_check_point of this CaseReportDetail.
        :type max_sent_bytes_check_point: float
        """
        self._max_sent_bytes_check_point = max_sent_bytes_check_point

    @property
    def max_sent_bytes_check_res(self):
        """Gets the max_sent_bytes_check_res of this CaseReportDetail.

        最大上行带宽检查结果

        :return: The max_sent_bytes_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._max_sent_bytes_check_res

    @max_sent_bytes_check_res.setter
    def max_sent_bytes_check_res(self, max_sent_bytes_check_res):
        """Sets the max_sent_bytes_check_res of this CaseReportDetail.

        最大上行带宽检查结果

        :param max_sent_bytes_check_res: The max_sent_bytes_check_res of this CaseReportDetail.
        :type max_sent_bytes_check_res: bool
        """
        self._max_sent_bytes_check_res = max_sent_bytes_check_res

    @property
    def max_success_rate(self):
        """Gets the max_success_rate of this CaseReportDetail.

        最大成功率

        :return: The max_success_rate of this CaseReportDetail.
        :rtype: float
        """
        return self._max_success_rate

    @max_success_rate.setter
    def max_success_rate(self, max_success_rate):
        """Sets the max_success_rate of this CaseReportDetail.

        最大成功率

        :param max_success_rate: The max_success_rate of this CaseReportDetail.
        :type max_success_rate: float
        """
        self._max_success_rate = max_success_rate

    @property
    def max_success_rate_check_res(self):
        """Gets the max_success_rate_check_res of this CaseReportDetail.

        最大成功率检查结果

        :return: The max_success_rate_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._max_success_rate_check_res

    @max_success_rate_check_res.setter
    def max_success_rate_check_res(self, max_success_rate_check_res):
        """Sets the max_success_rate_check_res of this CaseReportDetail.

        最大成功率检查结果

        :param max_success_rate_check_res: The max_success_rate_check_res of this CaseReportDetail.
        :type max_success_rate_check_res: bool
        """
        self._max_success_rate_check_res = max_success_rate_check_res

    @property
    def max_thread_num(self):
        """Gets the max_thread_num of this CaseReportDetail.

        最大线程数

        :return: The max_thread_num of this CaseReportDetail.
        :rtype: float
        """
        return self._max_thread_num

    @max_thread_num.setter
    def max_thread_num(self, max_thread_num):
        """Sets the max_thread_num of this CaseReportDetail.

        最大线程数

        :param max_thread_num: The max_thread_num of this CaseReportDetail.
        :type max_thread_num: float
        """
        self._max_thread_num = max_thread_num

    @property
    def max_thread_num_check_point(self):
        """Gets the max_thread_num_check_point of this CaseReportDetail.

        最大线程数检查点

        :return: The max_thread_num_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._max_thread_num_check_point

    @max_thread_num_check_point.setter
    def max_thread_num_check_point(self, max_thread_num_check_point):
        """Sets the max_thread_num_check_point of this CaseReportDetail.

        最大线程数检查点

        :param max_thread_num_check_point: The max_thread_num_check_point of this CaseReportDetail.
        :type max_thread_num_check_point: float
        """
        self._max_thread_num_check_point = max_thread_num_check_point

    @property
    def max_thread_num_check_res(self):
        """Gets the max_thread_num_check_res of this CaseReportDetail.

        最大线程数检查结果

        :return: The max_thread_num_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._max_thread_num_check_res

    @max_thread_num_check_res.setter
    def max_thread_num_check_res(self, max_thread_num_check_res):
        """Sets the max_thread_num_check_res of this CaseReportDetail.

        最大线程数检查结果

        :param max_thread_num_check_res: The max_thread_num_check_res of this CaseReportDetail.
        :type max_thread_num_check_res: bool
        """
        self._max_thread_num_check_res = max_thread_num_check_res

    @property
    def max_tps(self):
        """Gets the max_tps of this CaseReportDetail.

        最大TPS

        :return: The max_tps of this CaseReportDetail.
        :rtype: float
        """
        return self._max_tps

    @max_tps.setter
    def max_tps(self, max_tps):
        """Sets the max_tps of this CaseReportDetail.

        最大TPS

        :param max_tps: The max_tps of this CaseReportDetail.
        :type max_tps: float
        """
        self._max_tps = max_tps

    @property
    def max_tps_check_point(self):
        """Gets the max_tps_check_point of this CaseReportDetail.

        最大TPS检查点

        :return: The max_tps_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._max_tps_check_point

    @max_tps_check_point.setter
    def max_tps_check_point(self, max_tps_check_point):
        """Sets the max_tps_check_point of this CaseReportDetail.

        最大TPS检查点

        :param max_tps_check_point: The max_tps_check_point of this CaseReportDetail.
        :type max_tps_check_point: float
        """
        self._max_tps_check_point = max_tps_check_point

    @property
    def max_tps_check_res(self):
        """Gets the max_tps_check_res of this CaseReportDetail.

        最大TPS检查结果

        :return: The max_tps_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._max_tps_check_res

    @max_tps_check_res.setter
    def max_tps_check_res(self, max_tps_check_res):
        """Sets the max_tps_check_res of this CaseReportDetail.

        最大TPS检查结果

        :param max_tps_check_res: The max_tps_check_res of this CaseReportDetail.
        :type max_tps_check_res: bool
        """
        self._max_tps_check_res = max_tps_check_res

    @property
    def max_tran_resp_time(self):
        """Gets the max_tran_resp_time of this CaseReportDetail.

        最大事务响应时间

        :return: The max_tran_resp_time of this CaseReportDetail.
        :rtype: float
        """
        return self._max_tran_resp_time

    @max_tran_resp_time.setter
    def max_tran_resp_time(self, max_tran_resp_time):
        """Sets the max_tran_resp_time of this CaseReportDetail.

        最大事务响应时间

        :param max_tran_resp_time: The max_tran_resp_time of this CaseReportDetail.
        :type max_tran_resp_time: float
        """
        self._max_tran_resp_time = max_tran_resp_time

    @property
    def max_tran_resp_time_check_point(self):
        """Gets the max_tran_resp_time_check_point of this CaseReportDetail.

        最大事务响应时间检查点

        :return: The max_tran_resp_time_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._max_tran_resp_time_check_point

    @max_tran_resp_time_check_point.setter
    def max_tran_resp_time_check_point(self, max_tran_resp_time_check_point):
        """Sets the max_tran_resp_time_check_point of this CaseReportDetail.

        最大事务响应时间检查点

        :param max_tran_resp_time_check_point: The max_tran_resp_time_check_point of this CaseReportDetail.
        :type max_tran_resp_time_check_point: float
        """
        self._max_tran_resp_time_check_point = max_tran_resp_time_check_point

    @property
    def max_tran_resp_time_check_res(self):
        """Gets the max_tran_resp_time_check_res of this CaseReportDetail.

        最大事务响应时间检查结果

        :return: The max_tran_resp_time_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._max_tran_resp_time_check_res

    @max_tran_resp_time_check_res.setter
    def max_tran_resp_time_check_res(self, max_tran_resp_time_check_res):
        """Sets the max_tran_resp_time_check_res of this CaseReportDetail.

        最大事务响应时间检查结果

        :param max_tran_resp_time_check_res: The max_tran_resp_time_check_res of this CaseReportDetail.
        :type max_tran_resp_time_check_res: bool
        """
        self._max_tran_resp_time_check_res = max_tran_resp_time_check_res

    @property
    def memory_usage(self):
        """Gets the memory_usage of this CaseReportDetail.

        最大内存使用率

        :return: The memory_usage of this CaseReportDetail.
        :rtype: float
        """
        return self._memory_usage

    @memory_usage.setter
    def memory_usage(self, memory_usage):
        """Sets the memory_usage of this CaseReportDetail.

        最大内存使用率

        :param memory_usage: The memory_usage of this CaseReportDetail.
        :type memory_usage: float
        """
        self._memory_usage = memory_usage

    @property
    def memory_usage_avg(self):
        """Gets the memory_usage_avg of this CaseReportDetail.

        平均内存使用率

        :return: The memory_usage_avg of this CaseReportDetail.
        :rtype: float
        """
        return self._memory_usage_avg

    @memory_usage_avg.setter
    def memory_usage_avg(self, memory_usage_avg):
        """Sets the memory_usage_avg of this CaseReportDetail.

        平均内存使用率

        :param memory_usage_avg: The memory_usage_avg of this CaseReportDetail.
        :type memory_usage_avg: float
        """
        self._memory_usage_avg = memory_usage_avg

    @property
    def memory_usage_avg_check_point(self):
        """Gets the memory_usage_avg_check_point of this CaseReportDetail.

        平均内存使用率检查点

        :return: The memory_usage_avg_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._memory_usage_avg_check_point

    @memory_usage_avg_check_point.setter
    def memory_usage_avg_check_point(self, memory_usage_avg_check_point):
        """Sets the memory_usage_avg_check_point of this CaseReportDetail.

        平均内存使用率检查点

        :param memory_usage_avg_check_point: The memory_usage_avg_check_point of this CaseReportDetail.
        :type memory_usage_avg_check_point: float
        """
        self._memory_usage_avg_check_point = memory_usage_avg_check_point

    @property
    def memory_usage_avg_check_res(self):
        """Gets the memory_usage_avg_check_res of this CaseReportDetail.

        平均内存使用率检查结果

        :return: The memory_usage_avg_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._memory_usage_avg_check_res

    @memory_usage_avg_check_res.setter
    def memory_usage_avg_check_res(self, memory_usage_avg_check_res):
        """Sets the memory_usage_avg_check_res of this CaseReportDetail.

        平均内存使用率检查结果

        :param memory_usage_avg_check_res: The memory_usage_avg_check_res of this CaseReportDetail.
        :type memory_usage_avg_check_res: bool
        """
        self._memory_usage_avg_check_res = memory_usage_avg_check_res

    @property
    def memory_usage_check_point(self):
        """Gets the memory_usage_check_point of this CaseReportDetail.

        最大内存使用率检查点

        :return: The memory_usage_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._memory_usage_check_point

    @memory_usage_check_point.setter
    def memory_usage_check_point(self, memory_usage_check_point):
        """Sets the memory_usage_check_point of this CaseReportDetail.

        最大内存使用率检查点

        :param memory_usage_check_point: The memory_usage_check_point of this CaseReportDetail.
        :type memory_usage_check_point: float
        """
        self._memory_usage_check_point = memory_usage_check_point

    @property
    def memory_usage_check_res(self):
        """Gets the memory_usage_check_res of this CaseReportDetail.

        最大内存使用率检查结果

        :return: The memory_usage_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._memory_usage_check_res

    @memory_usage_check_res.setter
    def memory_usage_check_res(self, memory_usage_check_res):
        """Sets the memory_usage_check_res of this CaseReportDetail.

        最大内存使用率检查结果

        :param memory_usage_check_res: The memory_usage_check_res of this CaseReportDetail.
        :type memory_usage_check_res: bool
        """
        self._memory_usage_check_res = memory_usage_check_res

    @property
    def min(self):
        """Gets the min of this CaseReportDetail.

        最小响应时间

        :return: The min of this CaseReportDetail.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this CaseReportDetail.

        最小响应时间

        :param min: The min of this CaseReportDetail.
        :type min: int
        """
        self._min = min

    @property
    def min_network_traffic(self):
        """Gets the min_network_traffic of this CaseReportDetail.

        流量谷值

        :return: The min_network_traffic of this CaseReportDetail.
        :rtype: int
        """
        return self._min_network_traffic

    @min_network_traffic.setter
    def min_network_traffic(self, min_network_traffic):
        """Sets the min_network_traffic of this CaseReportDetail.

        流量谷值

        :param min_network_traffic: The min_network_traffic of this CaseReportDetail.
        :type min_network_traffic: int
        """
        self._min_network_traffic = min_network_traffic

    @property
    def mode(self):
        """Gets the mode of this CaseReportDetail.

        压力模式

        :return: The mode of this CaseReportDetail.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this CaseReportDetail.

        压力模式

        :param mode: The mode of this CaseReportDetail.
        :type mode: str
        """
        self._mode = mode

    @property
    def monitor_peak_time(self):
        """Gets the monitor_peak_time of this CaseReportDetail.

        监控峰值时间

        :return: The monitor_peak_time of this CaseReportDetail.
        :rtype: float
        """
        return self._monitor_peak_time

    @monitor_peak_time.setter
    def monitor_peak_time(self, monitor_peak_time):
        """Sets the monitor_peak_time of this CaseReportDetail.

        监控峰值时间

        :param monitor_peak_time: The monitor_peak_time of this CaseReportDetail.
        :type monitor_peak_time: float
        """
        self._monitor_peak_time = monitor_peak_time

    @property
    def monitor_peak_time_check_point(self):
        """Gets the monitor_peak_time_check_point of this CaseReportDetail.

        监控峰值时间检查点

        :return: The monitor_peak_time_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._monitor_peak_time_check_point

    @monitor_peak_time_check_point.setter
    def monitor_peak_time_check_point(self, monitor_peak_time_check_point):
        """Sets the monitor_peak_time_check_point of this CaseReportDetail.

        监控峰值时间检查点

        :param monitor_peak_time_check_point: The monitor_peak_time_check_point of this CaseReportDetail.
        :type monitor_peak_time_check_point: float
        """
        self._monitor_peak_time_check_point = monitor_peak_time_check_point

    @property
    def monitor_peak_time_check_res(self):
        """Gets the monitor_peak_time_check_res of this CaseReportDetail.

        监控峰值时间检查结果

        :return: The monitor_peak_time_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._monitor_peak_time_check_res

    @monitor_peak_time_check_res.setter
    def monitor_peak_time_check_res(self, monitor_peak_time_check_res):
        """Sets the monitor_peak_time_check_res of this CaseReportDetail.

        监控峰值时间检查结果

        :param monitor_peak_time_check_res: The monitor_peak_time_check_res of this CaseReportDetail.
        :type monitor_peak_time_check_res: bool
        """
        self._monitor_peak_time_check_res = monitor_peak_time_check_res

    @property
    def monitor_result(self):
        """Gets the monitor_result of this CaseReportDetail.

        监控结果

        :return: The monitor_result of this CaseReportDetail.
        :rtype: float
        """
        return self._monitor_result

    @monitor_result.setter
    def monitor_result(self, monitor_result):
        """Sets the monitor_result of this CaseReportDetail.

        监控结果

        :param monitor_result: The monitor_result of this CaseReportDetail.
        :type monitor_result: float
        """
        self._monitor_result = monitor_result

    @property
    def monitor_result_check_point(self):
        """Gets the monitor_result_check_point of this CaseReportDetail.

        监控结果检查点

        :return: The monitor_result_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._monitor_result_check_point

    @monitor_result_check_point.setter
    def monitor_result_check_point(self, monitor_result_check_point):
        """Sets the monitor_result_check_point of this CaseReportDetail.

        监控结果检查点

        :param monitor_result_check_point: The monitor_result_check_point of this CaseReportDetail.
        :type monitor_result_check_point: float
        """
        self._monitor_result_check_point = monitor_result_check_point

    @property
    def monitor_result_check_res(self):
        """Gets the monitor_result_check_res of this CaseReportDetail.

        监控结果检查结果

        :return: The monitor_result_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._monitor_result_check_res

    @monitor_result_check_res.setter
    def monitor_result_check_res(self, monitor_result_check_res):
        """Sets the monitor_result_check_res of this CaseReportDetail.

        监控结果检查结果

        :param monitor_result_check_res: The monitor_result_check_res of this CaseReportDetail.
        :type monitor_result_check_res: bool
        """
        self._monitor_result_check_res = monitor_result_check_res

    @property
    def name(self):
        """Gets the name of this CaseReportDetail.

        用例/aw/事务名

        :return: The name of this CaseReportDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CaseReportDetail.

        用例/aw/事务名

        :param name: The name of this CaseReportDetail.
        :type name: str
        """
        self._name = name

    @property
    def network_read(self):
        """Gets the network_read of this CaseReportDetail.

        网络最大接收数据速度

        :return: The network_read of this CaseReportDetail.
        :rtype: float
        """
        return self._network_read

    @network_read.setter
    def network_read(self, network_read):
        """Sets the network_read of this CaseReportDetail.

        网络最大接收数据速度

        :param network_read: The network_read of this CaseReportDetail.
        :type network_read: float
        """
        self._network_read = network_read

    @property
    def network_read_avg(self):
        """Gets the network_read_avg of this CaseReportDetail.

        网络平均接收数据速度

        :return: The network_read_avg of this CaseReportDetail.
        :rtype: float
        """
        return self._network_read_avg

    @network_read_avg.setter
    def network_read_avg(self, network_read_avg):
        """Sets the network_read_avg of this CaseReportDetail.

        网络平均接收数据速度

        :param network_read_avg: The network_read_avg of this CaseReportDetail.
        :type network_read_avg: float
        """
        self._network_read_avg = network_read_avg

    @property
    def network_read_avg_check_point(self):
        """Gets the network_read_avg_check_point of this CaseReportDetail.

        网络平均接收数据速度检查点

        :return: The network_read_avg_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._network_read_avg_check_point

    @network_read_avg_check_point.setter
    def network_read_avg_check_point(self, network_read_avg_check_point):
        """Sets the network_read_avg_check_point of this CaseReportDetail.

        网络平均接收数据速度检查点

        :param network_read_avg_check_point: The network_read_avg_check_point of this CaseReportDetail.
        :type network_read_avg_check_point: float
        """
        self._network_read_avg_check_point = network_read_avg_check_point

    @property
    def network_read_avg_check_res(self):
        """Gets the network_read_avg_check_res of this CaseReportDetail.

        网络平均接收数据速度检查结果

        :return: The network_read_avg_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._network_read_avg_check_res

    @network_read_avg_check_res.setter
    def network_read_avg_check_res(self, network_read_avg_check_res):
        """Sets the network_read_avg_check_res of this CaseReportDetail.

        网络平均接收数据速度检查结果

        :param network_read_avg_check_res: The network_read_avg_check_res of this CaseReportDetail.
        :type network_read_avg_check_res: bool
        """
        self._network_read_avg_check_res = network_read_avg_check_res

    @property
    def network_read_check_point(self):
        """Gets the network_read_check_point of this CaseReportDetail.

        网络最大接收数据速度检查点

        :return: The network_read_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._network_read_check_point

    @network_read_check_point.setter
    def network_read_check_point(self, network_read_check_point):
        """Sets the network_read_check_point of this CaseReportDetail.

        网络最大接收数据速度检查点

        :param network_read_check_point: The network_read_check_point of this CaseReportDetail.
        :type network_read_check_point: float
        """
        self._network_read_check_point = network_read_check_point

    @property
    def network_read_check_res(self):
        """Gets the network_read_check_res of this CaseReportDetail.

        网络最大接收数据速度检查结果

        :return: The network_read_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._network_read_check_res

    @network_read_check_res.setter
    def network_read_check_res(self, network_read_check_res):
        """Sets the network_read_check_res of this CaseReportDetail.

        网络最大接收数据速度检查结果

        :param network_read_check_res: The network_read_check_res of this CaseReportDetail.
        :type network_read_check_res: bool
        """
        self._network_read_check_res = network_read_check_res

    @property
    def network_write(self):
        """Gets the network_write of this CaseReportDetail.

        网络最大写入数据速度

        :return: The network_write of this CaseReportDetail.
        :rtype: float
        """
        return self._network_write

    @network_write.setter
    def network_write(self, network_write):
        """Sets the network_write of this CaseReportDetail.

        网络最大写入数据速度

        :param network_write: The network_write of this CaseReportDetail.
        :type network_write: float
        """
        self._network_write = network_write

    @property
    def network_write_avg(self):
        """Gets the network_write_avg of this CaseReportDetail.

        网络平均写入数据速度

        :return: The network_write_avg of this CaseReportDetail.
        :rtype: float
        """
        return self._network_write_avg

    @network_write_avg.setter
    def network_write_avg(self, network_write_avg):
        """Sets the network_write_avg of this CaseReportDetail.

        网络平均写入数据速度

        :param network_write_avg: The network_write_avg of this CaseReportDetail.
        :type network_write_avg: float
        """
        self._network_write_avg = network_write_avg

    @property
    def network_write_avg_check_point(self):
        """Gets the network_write_avg_check_point of this CaseReportDetail.

        网络平均写入数据速度检查点

        :return: The network_write_avg_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._network_write_avg_check_point

    @network_write_avg_check_point.setter
    def network_write_avg_check_point(self, network_write_avg_check_point):
        """Sets the network_write_avg_check_point of this CaseReportDetail.

        网络平均写入数据速度检查点

        :param network_write_avg_check_point: The network_write_avg_check_point of this CaseReportDetail.
        :type network_write_avg_check_point: float
        """
        self._network_write_avg_check_point = network_write_avg_check_point

    @property
    def network_write_avg_check_res(self):
        """Gets the network_write_avg_check_res of this CaseReportDetail.

        网络平均写入数据速度检查结果

        :return: The network_write_avg_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._network_write_avg_check_res

    @network_write_avg_check_res.setter
    def network_write_avg_check_res(self, network_write_avg_check_res):
        """Sets the network_write_avg_check_res of this CaseReportDetail.

        网络平均写入数据速度检查结果

        :param network_write_avg_check_res: The network_write_avg_check_res of this CaseReportDetail.
        :type network_write_avg_check_res: bool
        """
        self._network_write_avg_check_res = network_write_avg_check_res

    @property
    def network_write_check_point(self):
        """Gets the network_write_check_point of this CaseReportDetail.

        网络最大写入数据速度检查点

        :return: The network_write_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._network_write_check_point

    @network_write_check_point.setter
    def network_write_check_point(self, network_write_check_point):
        """Sets the network_write_check_point of this CaseReportDetail.

        网络最大写入数据速度检查点

        :param network_write_check_point: The network_write_check_point of this CaseReportDetail.
        :type network_write_check_point: float
        """
        self._network_write_check_point = network_write_check_point

    @property
    def network_write_check_res(self):
        """Gets the network_write_check_res of this CaseReportDetail.

        网络最大写入数据速度检查结果

        :return: The network_write_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._network_write_check_res

    @network_write_check_res.setter
    def network_write_check_res(self, network_write_check_res):
        """Sets the network_write_check_res of this CaseReportDetail.

        网络最大写入数据速度检查结果

        :param network_write_check_res: The network_write_check_res of this CaseReportDetail.
        :type network_write_check_res: bool
        """
        self._network_write_check_res = network_write_check_res

    @property
    def peak_load_status(self):
        """Gets the peak_load_status of this CaseReportDetail.

        峰值负载状态

        :return: The peak_load_status of this CaseReportDetail.
        :rtype: float
        """
        return self._peak_load_status

    @peak_load_status.setter
    def peak_load_status(self, peak_load_status):
        """Sets the peak_load_status of this CaseReportDetail.

        峰值负载状态

        :param peak_load_status: The peak_load_status of this CaseReportDetail.
        :type peak_load_status: float
        """
        self._peak_load_status = peak_load_status

    @property
    def peak_load_status_check_point(self):
        """Gets the peak_load_status_check_point of this CaseReportDetail.

        峰值负载状态检查点

        :return: The peak_load_status_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._peak_load_status_check_point

    @peak_load_status_check_point.setter
    def peak_load_status_check_point(self, peak_load_status_check_point):
        """Sets the peak_load_status_check_point of this CaseReportDetail.

        峰值负载状态检查点

        :param peak_load_status_check_point: The peak_load_status_check_point of this CaseReportDetail.
        :type peak_load_status_check_point: float
        """
        self._peak_load_status_check_point = peak_load_status_check_point

    @property
    def peak_load_status_check_res(self):
        """Gets the peak_load_status_check_res of this CaseReportDetail.

        峰值负载状态检查结果

        :return: The peak_load_status_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._peak_load_status_check_res

    @peak_load_status_check_res.setter
    def peak_load_status_check_res(self, peak_load_status_check_res):
        """Sets the peak_load_status_check_res of this CaseReportDetail.

        峰值负载状态检查结果

        :param peak_load_status_check_res: The peak_load_status_check_res of this CaseReportDetail.
        :type peak_load_status_check_res: bool
        """
        self._peak_load_status_check_res = peak_load_status_check_res

    @property
    def peak_metric(self):
        """Gets the peak_metric of this CaseReportDetail.

        :return: The peak_metric of this CaseReportDetail.
        :rtype: :class:`huaweicloudsdkcpts.v1.PeakMetric`
        """
        return self._peak_metric

    @peak_metric.setter
    def peak_metric(self, peak_metric):
        """Sets the peak_metric of this CaseReportDetail.

        :param peak_metric: The peak_metric of this CaseReportDetail.
        :type peak_metric: :class:`huaweicloudsdkcpts.v1.PeakMetric`
        """
        self._peak_metric = peak_metric

    @property
    def project_id(self):
        """Gets the project_id of this CaseReportDetail.

        工程ID

        :return: The project_id of this CaseReportDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CaseReportDetail.

        工程ID

        :param project_id: The project_id of this CaseReportDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def protocols(self):
        """Gets the protocols of this CaseReportDetail.

        协议

        :return: The protocols of this CaseReportDetail.
        :rtype: list[str]
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        """Sets the protocols of this CaseReportDetail.

        协议

        :param protocols: The protocols of this CaseReportDetail.
        :type protocols: list[str]
        """
        self._protocols = protocols

    @property
    def requests(self):
        """Gets the requests of this CaseReportDetail.

        请求数

        :return: The requests of this CaseReportDetail.
        :rtype: int
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        """Sets the requests of this CaseReportDetail.

        请求数

        :param requests: The requests of this CaseReportDetail.
        :type requests: int
        """
        self._requests = requests

    @property
    def result(self):
        """Gets the result of this CaseReportDetail.

        用例结果

        :return: The result of this CaseReportDetail.
        :rtype: int
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this CaseReportDetail.

        用例结果

        :param result: The result of this CaseReportDetail.
        :type result: int
        """
        self._result = result

    @property
    def result_log(self):
        """Gets the result_log of this CaseReportDetail.

        用例结果日志

        :return: The result_log of this CaseReportDetail.
        :rtype: str
        """
        return self._result_log

    @result_log.setter
    def result_log(self, result_log):
        """Sets the result_log of this CaseReportDetail.

        用例结果日志

        :param result_log: The result_log of this CaseReportDetail.
        :type result_log: str
        """
        self._result_log = result_log

    @property
    def round(self):
        """Gets the round of this CaseReportDetail.

        执行轮次

        :return: The round of this CaseReportDetail.
        :rtype: int
        """
        return self._round

    @round.setter
    def round(self, round):
        """Sets the round of this CaseReportDetail.

        执行轮次

        :param round: The round of this CaseReportDetail.
        :type round: int
        """
        self._round = round

    @property
    def save_all_data(self):
        """Gets the save_all_data of this CaseReportDetail.

        是否存储全量数据到CSS

        :return: The save_all_data of this CaseReportDetail.
        :rtype: bool
        """
        return self._save_all_data

    @save_all_data.setter
    def save_all_data(self, save_all_data):
        """Sets the save_all_data of this CaseReportDetail.

        是否存储全量数据到CSS

        :param save_all_data: The save_all_data of this CaseReportDetail.
        :type save_all_data: bool
        """
        self._save_all_data = save_all_data

    @property
    def service_id(self):
        """Gets the service_id of this CaseReportDetail.

        服务ID

        :return: The service_id of this CaseReportDetail.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this CaseReportDetail.

        服务ID

        :param service_id: The service_id of this CaseReportDetail.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def stage(self):
        """Gets the stage of this CaseReportDetail.

        阶段

        :return: The stage of this CaseReportDetail.
        :rtype: int
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this CaseReportDetail.

        阶段

        :param stage: The stage of this CaseReportDetail.
        :type stage: int
        """
        self._stage = stage

    @property
    def start_time(self):
        """Gets the start_time of this CaseReportDetail.

        开始时间

        :return: The start_time of this CaseReportDetail.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this CaseReportDetail.

        开始时间

        :param start_time: The start_time of this CaseReportDetail.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this CaseReportDetail.

        任务状态

        :return: The status of this CaseReportDetail.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CaseReportDetail.

        任务状态

        :param status: The status of this CaseReportDetail.
        :type status: int
        """
        self._status = status

    @property
    def streaming_media_vo(self):
        """Gets the streaming_media_vo of this CaseReportDetail.

        :return: The streaming_media_vo of this CaseReportDetail.
        :rtype: :class:`huaweicloudsdkcpts.v1.StreamingMediaReport`
        """
        return self._streaming_media_vo

    @streaming_media_vo.setter
    def streaming_media_vo(self, streaming_media_vo):
        """Sets the streaming_media_vo of this CaseReportDetail.

        :param streaming_media_vo: The streaming_media_vo of this CaseReportDetail.
        :type streaming_media_vo: :class:`huaweicloudsdkcpts.v1.StreamingMediaReport`
        """
        self._streaming_media_vo = streaming_media_vo

    @property
    def success_count(self):
        """Gets the success_count of this CaseReportDetail.

        成功数

        :return: The success_count of this CaseReportDetail.
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        """Sets the success_count of this CaseReportDetail.

        成功数

        :param success_count: The success_count of this CaseReportDetail.
        :type success_count: int
        """
        self._success_count = success_count

    @property
    def success_rate(self):
        """Gets the success_rate of this CaseReportDetail.

        成功率

        :return: The success_rate of this CaseReportDetail.
        :rtype: int
        """
        return self._success_rate

    @success_rate.setter
    def success_rate(self, success_rate):
        """Sets the success_rate of this CaseReportDetail.

        成功率

        :param success_rate: The success_rate of this CaseReportDetail.
        :type success_rate: int
        """
        self._success_rate = success_rate

    @property
    def success_rate_check_point(self):
        """Gets the success_rate_check_point of this CaseReportDetail.

        成功率检查点

        :return: The success_rate_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._success_rate_check_point

    @success_rate_check_point.setter
    def success_rate_check_point(self, success_rate_check_point):
        """Sets the success_rate_check_point of this CaseReportDetail.

        成功率检查点

        :param success_rate_check_point: The success_rate_check_point of this CaseReportDetail.
        :type success_rate_check_point: float
        """
        self._success_rate_check_point = success_rate_check_point

    @property
    def success_rate_check_res(self):
        """Gets the success_rate_check_res of this CaseReportDetail.

        成功率检查结果

        :return: The success_rate_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._success_rate_check_res

    @success_rate_check_res.setter
    def success_rate_check_res(self, success_rate_check_res):
        """Sets the success_rate_check_res of this CaseReportDetail.

        成功率检查结果

        :param success_rate_check_res: The success_rate_check_res of this CaseReportDetail.
        :type success_rate_check_res: bool
        """
        self._success_rate_check_res = success_rate_check_res

    @property
    def sum1xx(self):
        """Gets the sum1xx of this CaseReportDetail.

        1XX响应码数量

        :return: The sum1xx of this CaseReportDetail.
        :rtype: int
        """
        return self._sum1xx

    @sum1xx.setter
    def sum1xx(self, sum1xx):
        """Sets the sum1xx of this CaseReportDetail.

        1XX响应码数量

        :param sum1xx: The sum1xx of this CaseReportDetail.
        :type sum1xx: int
        """
        self._sum1xx = sum1xx

    @property
    def sum2xx(self):
        """Gets the sum2xx of this CaseReportDetail.

        2XX响应码数量

        :return: The sum2xx of this CaseReportDetail.
        :rtype: int
        """
        return self._sum2xx

    @sum2xx.setter
    def sum2xx(self, sum2xx):
        """Sets the sum2xx of this CaseReportDetail.

        2XX响应码数量

        :param sum2xx: The sum2xx of this CaseReportDetail.
        :type sum2xx: int
        """
        self._sum2xx = sum2xx

    @property
    def sum3xx(self):
        """Gets the sum3xx of this CaseReportDetail.

        3XX响应码数量

        :return: The sum3xx of this CaseReportDetail.
        :rtype: int
        """
        return self._sum3xx

    @sum3xx.setter
    def sum3xx(self, sum3xx):
        """Sets the sum3xx of this CaseReportDetail.

        3XX响应码数量

        :param sum3xx: The sum3xx of this CaseReportDetail.
        :type sum3xx: int
        """
        self._sum3xx = sum3xx

    @property
    def sum4xx(self):
        """Gets the sum4xx of this CaseReportDetail.

        4XX响应码数量

        :return: The sum4xx of this CaseReportDetail.
        :rtype: int
        """
        return self._sum4xx

    @sum4xx.setter
    def sum4xx(self, sum4xx):
        """Sets the sum4xx of this CaseReportDetail.

        4XX响应码数量

        :param sum4xx: The sum4xx of this CaseReportDetail.
        :type sum4xx: int
        """
        self._sum4xx = sum4xx

    @property
    def sum5xx(self):
        """Gets the sum5xx of this CaseReportDetail.

        5XX响应码数量

        :return: The sum5xx of this CaseReportDetail.
        :rtype: int
        """
        return self._sum5xx

    @sum5xx.setter
    def sum5xx(self, sum5xx):
        """Sets the sum5xx of this CaseReportDetail.

        5XX响应码数量

        :param sum5xx: The sum5xx of this CaseReportDetail.
        :type sum5xx: int
        """
        self._sum5xx = sum5xx

    @property
    def task_id(self):
        """Gets the task_id of this CaseReportDetail.

        任务ID

        :return: The task_id of this CaseReportDetail.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this CaseReportDetail.

        任务ID

        :param task_id: The task_id of this CaseReportDetail.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        """Gets the task_name of this CaseReportDetail.

        任务名

        :return: The task_name of this CaseReportDetail.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this CaseReportDetail.

        任务名

        :param task_name: The task_name of this CaseReportDetail.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_project_id(self):
        """Gets the task_project_id of this CaseReportDetail.

        任务项目ID

        :return: The task_project_id of this CaseReportDetail.
        :rtype: str
        """
        return self._task_project_id

    @task_project_id.setter
    def task_project_id(self, task_project_id):
        """Sets the task_project_id of this CaseReportDetail.

        任务项目ID

        :param task_project_id: The task_project_id of this CaseReportDetail.
        :type task_project_id: str
        """
        self._task_project_id = task_project_id

    @property
    def task_status(self):
        """Gets the task_status of this CaseReportDetail.

        任务状态

        :return: The task_status of this CaseReportDetail.
        :rtype: int
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this CaseReportDetail.

        任务状态

        :param task_status: The task_status of this CaseReportDetail.
        :type task_status: int
        """
        self._task_status = task_status

    @property
    def test_case_uri(self):
        """Gets the test_case_uri of this CaseReportDetail.

        用例基线uri

        :return: The test_case_uri of this CaseReportDetail.
        :rtype: str
        """
        return self._test_case_uri

    @test_case_uri.setter
    def test_case_uri(self, test_case_uri):
        """Sets the test_case_uri of this CaseReportDetail.

        用例基线uri

        :param test_case_uri: The test_case_uri of this CaseReportDetail.
        :type test_case_uri: str
        """
        self._test_case_uri = test_case_uri

    @property
    def tp50(self):
        """Gets the tp50 of this CaseReportDetail.

        TP50

        :return: The tp50 of this CaseReportDetail.
        :rtype: int
        """
        return self._tp50

    @tp50.setter
    def tp50(self, tp50):
        """Sets the tp50 of this CaseReportDetail.

        TP50

        :param tp50: The tp50 of this CaseReportDetail.
        :type tp50: int
        """
        self._tp50 = tp50

    @property
    def tp50_check_point(self):
        """Gets the tp50_check_point of this CaseReportDetail.

        TP50检查点

        :return: The tp50_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._tp50_check_point

    @tp50_check_point.setter
    def tp50_check_point(self, tp50_check_point):
        """Sets the tp50_check_point of this CaseReportDetail.

        TP50检查点

        :param tp50_check_point: The tp50_check_point of this CaseReportDetail.
        :type tp50_check_point: float
        """
        self._tp50_check_point = tp50_check_point

    @property
    def tp50_check_res(self):
        """Gets the tp50_check_res of this CaseReportDetail.

        TP50检查结果

        :return: The tp50_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._tp50_check_res

    @tp50_check_res.setter
    def tp50_check_res(self, tp50_check_res):
        """Sets the tp50_check_res of this CaseReportDetail.

        TP50检查结果

        :param tp50_check_res: The tp50_check_res of this CaseReportDetail.
        :type tp50_check_res: bool
        """
        self._tp50_check_res = tp50_check_res

    @property
    def tp75(self):
        """Gets the tp75 of this CaseReportDetail.

        TP75

        :return: The tp75 of this CaseReportDetail.
        :rtype: int
        """
        return self._tp75

    @tp75.setter
    def tp75(self, tp75):
        """Sets the tp75 of this CaseReportDetail.

        TP75

        :param tp75: The tp75 of this CaseReportDetail.
        :type tp75: int
        """
        self._tp75 = tp75

    @property
    def tp75_check_point(self):
        """Gets the tp75_check_point of this CaseReportDetail.

        TP75检查点

        :return: The tp75_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._tp75_check_point

    @tp75_check_point.setter
    def tp75_check_point(self, tp75_check_point):
        """Sets the tp75_check_point of this CaseReportDetail.

        TP75检查点

        :param tp75_check_point: The tp75_check_point of this CaseReportDetail.
        :type tp75_check_point: float
        """
        self._tp75_check_point = tp75_check_point

    @property
    def tp75_check_res(self):
        """Gets the tp75_check_res of this CaseReportDetail.

        TP75检查结果

        :return: The tp75_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._tp75_check_res

    @tp75_check_res.setter
    def tp75_check_res(self, tp75_check_res):
        """Sets the tp75_check_res of this CaseReportDetail.

        TP75检查结果

        :param tp75_check_res: The tp75_check_res of this CaseReportDetail.
        :type tp75_check_res: bool
        """
        self._tp75_check_res = tp75_check_res

    @property
    def tp85(self):
        """Gets the tp85 of this CaseReportDetail.

        TP85

        :return: The tp85 of this CaseReportDetail.
        :rtype: int
        """
        return self._tp85

    @tp85.setter
    def tp85(self, tp85):
        """Sets the tp85 of this CaseReportDetail.

        TP85

        :param tp85: The tp85 of this CaseReportDetail.
        :type tp85: int
        """
        self._tp85 = tp85

    @property
    def tp85_check_point(self):
        """Gets the tp85_check_point of this CaseReportDetail.

        TP85检查点

        :return: The tp85_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._tp85_check_point

    @tp85_check_point.setter
    def tp85_check_point(self, tp85_check_point):
        """Sets the tp85_check_point of this CaseReportDetail.

        TP85检查点

        :param tp85_check_point: The tp85_check_point of this CaseReportDetail.
        :type tp85_check_point: float
        """
        self._tp85_check_point = tp85_check_point

    @property
    def tp85_check_res(self):
        """Gets the tp85_check_res of this CaseReportDetail.

        TP85检查结果

        :return: The tp85_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._tp85_check_res

    @tp85_check_res.setter
    def tp85_check_res(self, tp85_check_res):
        """Sets the tp85_check_res of this CaseReportDetail.

        TP85检查结果

        :param tp85_check_res: The tp85_check_res of this CaseReportDetail.
        :type tp85_check_res: bool
        """
        self._tp85_check_res = tp85_check_res

    @property
    def tp90(self):
        """Gets the tp90 of this CaseReportDetail.

        TP90

        :return: The tp90 of this CaseReportDetail.
        :rtype: int
        """
        return self._tp90

    @tp90.setter
    def tp90(self, tp90):
        """Sets the tp90 of this CaseReportDetail.

        TP90

        :param tp90: The tp90 of this CaseReportDetail.
        :type tp90: int
        """
        self._tp90 = tp90

    @property
    def tp90_check_point(self):
        """Gets the tp90_check_point of this CaseReportDetail.

        TP90检查点

        :return: The tp90_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._tp90_check_point

    @tp90_check_point.setter
    def tp90_check_point(self, tp90_check_point):
        """Sets the tp90_check_point of this CaseReportDetail.

        TP90检查点

        :param tp90_check_point: The tp90_check_point of this CaseReportDetail.
        :type tp90_check_point: float
        """
        self._tp90_check_point = tp90_check_point

    @property
    def tp90_check_res(self):
        """Gets the tp90_check_res of this CaseReportDetail.

        TP90检查结果

        :return: The tp90_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._tp90_check_res

    @tp90_check_res.setter
    def tp90_check_res(self, tp90_check_res):
        """Sets the tp90_check_res of this CaseReportDetail.

        TP90检查结果

        :param tp90_check_res: The tp90_check_res of this CaseReportDetail.
        :type tp90_check_res: bool
        """
        self._tp90_check_res = tp90_check_res

    @property
    def tp95(self):
        """Gets the tp95 of this CaseReportDetail.

        TP95

        :return: The tp95 of this CaseReportDetail.
        :rtype: int
        """
        return self._tp95

    @tp95.setter
    def tp95(self, tp95):
        """Sets the tp95 of this CaseReportDetail.

        TP95

        :param tp95: The tp95 of this CaseReportDetail.
        :type tp95: int
        """
        self._tp95 = tp95

    @property
    def tp95_check_point(self):
        """Gets the tp95_check_point of this CaseReportDetail.

        TP95检查点

        :return: The tp95_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._tp95_check_point

    @tp95_check_point.setter
    def tp95_check_point(self, tp95_check_point):
        """Sets the tp95_check_point of this CaseReportDetail.

        TP95检查点

        :param tp95_check_point: The tp95_check_point of this CaseReportDetail.
        :type tp95_check_point: float
        """
        self._tp95_check_point = tp95_check_point

    @property
    def tp95_check_res(self):
        """Gets the tp95_check_res of this CaseReportDetail.

        TP95检查结果

        :return: The tp95_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._tp95_check_res

    @tp95_check_res.setter
    def tp95_check_res(self, tp95_check_res):
        """Sets the tp95_check_res of this CaseReportDetail.

        TP95检查结果

        :param tp95_check_res: The tp95_check_res of this CaseReportDetail.
        :type tp95_check_res: bool
        """
        self._tp95_check_res = tp95_check_res

    @property
    def tp99(self):
        """Gets the tp99 of this CaseReportDetail.

        TP99

        :return: The tp99 of this CaseReportDetail.
        :rtype: int
        """
        return self._tp99

    @tp99.setter
    def tp99(self, tp99):
        """Sets the tp99 of this CaseReportDetail.

        TP99

        :param tp99: The tp99 of this CaseReportDetail.
        :type tp99: int
        """
        self._tp99 = tp99

    @property
    def tp999(self):
        """Gets the tp999 of this CaseReportDetail.

        TP99.9

        :return: The tp999 of this CaseReportDetail.
        :rtype: int
        """
        return self._tp999

    @tp999.setter
    def tp999(self, tp999):
        """Sets the tp999 of this CaseReportDetail.

        TP99.9

        :param tp999: The tp999 of this CaseReportDetail.
        :type tp999: int
        """
        self._tp999 = tp999

    @property
    def tp9999(self):
        """Gets the tp9999 of this CaseReportDetail.

        TP99.99

        :return: The tp9999 of this CaseReportDetail.
        :rtype: int
        """
        return self._tp9999

    @tp9999.setter
    def tp9999(self, tp9999):
        """Sets the tp9999 of this CaseReportDetail.

        TP99.99

        :param tp9999: The tp9999 of this CaseReportDetail.
        :type tp9999: int
        """
        self._tp9999 = tp9999

    @property
    def tp9999_check_point(self):
        """Gets the tp9999_check_point of this CaseReportDetail.

        TP99.99检查点

        :return: The tp9999_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._tp9999_check_point

    @tp9999_check_point.setter
    def tp9999_check_point(self, tp9999_check_point):
        """Sets the tp9999_check_point of this CaseReportDetail.

        TP99.99检查点

        :param tp9999_check_point: The tp9999_check_point of this CaseReportDetail.
        :type tp9999_check_point: float
        """
        self._tp9999_check_point = tp9999_check_point

    @property
    def tp9999_check_res(self):
        """Gets the tp9999_check_res of this CaseReportDetail.

        TP99.99检查结果

        :return: The tp9999_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._tp9999_check_res

    @tp9999_check_res.setter
    def tp9999_check_res(self, tp9999_check_res):
        """Sets the tp9999_check_res of this CaseReportDetail.

        TP99.99检查结果

        :param tp9999_check_res: The tp9999_check_res of this CaseReportDetail.
        :type tp9999_check_res: bool
        """
        self._tp9999_check_res = tp9999_check_res

    @property
    def tp999_check_point(self):
        """Gets the tp999_check_point of this CaseReportDetail.

        TP99.9检查点

        :return: The tp999_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._tp999_check_point

    @tp999_check_point.setter
    def tp999_check_point(self, tp999_check_point):
        """Sets the tp999_check_point of this CaseReportDetail.

        TP99.9检查点

        :param tp999_check_point: The tp999_check_point of this CaseReportDetail.
        :type tp999_check_point: float
        """
        self._tp999_check_point = tp999_check_point

    @property
    def tp999_check_res(self):
        """Gets the tp999_check_res of this CaseReportDetail.

        TP99.9检查结果

        :return: The tp999_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._tp999_check_res

    @tp999_check_res.setter
    def tp999_check_res(self, tp999_check_res):
        """Sets the tp999_check_res of this CaseReportDetail.

        TP99.9检查结果

        :param tp999_check_res: The tp999_check_res of this CaseReportDetail.
        :type tp999_check_res: bool
        """
        self._tp999_check_res = tp999_check_res

    @property
    def tp99_check_point(self):
        """Gets the tp99_check_point of this CaseReportDetail.

        TP99检查点

        :return: The tp99_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._tp99_check_point

    @tp99_check_point.setter
    def tp99_check_point(self, tp99_check_point):
        """Sets the tp99_check_point of this CaseReportDetail.

        TP99检查点

        :param tp99_check_point: The tp99_check_point of this CaseReportDetail.
        :type tp99_check_point: float
        """
        self._tp99_check_point = tp99_check_point

    @property
    def tp99_check_res(self):
        """Gets the tp99_check_res of this CaseReportDetail.

        TP99检查结果

        :return: The tp99_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._tp99_check_res

    @tp99_check_res.setter
    def tp99_check_res(self, tp99_check_res):
        """Sets the tp99_check_res of this CaseReportDetail.

        TP99检查结果

        :param tp99_check_res: The tp99_check_res of this CaseReportDetail.
        :type tp99_check_res: bool
        """
        self._tp99_check_res = tp99_check_res

    @property
    def tps(self):
        """Gets the tps of this CaseReportDetail.

        TPS

        :return: The tps of this CaseReportDetail.
        :rtype: float
        """
        return self._tps

    @tps.setter
    def tps(self, tps):
        """Sets the tps of this CaseReportDetail.

        TPS

        :param tps: The tps of this CaseReportDetail.
        :type tps: float
        """
        self._tps = tps

    @property
    def tps_check_point(self):
        """Gets the tps_check_point of this CaseReportDetail.

        TPS检查点

        :return: The tps_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._tps_check_point

    @tps_check_point.setter
    def tps_check_point(self, tps_check_point):
        """Sets the tps_check_point of this CaseReportDetail.

        TPS检查点

        :param tps_check_point: The tps_check_point of this CaseReportDetail.
        :type tps_check_point: float
        """
        self._tps_check_point = tps_check_point

    @property
    def tps_check_res(self):
        """Gets the tps_check_res of this CaseReportDetail.

        TPS检查结果

        :return: The tps_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._tps_check_res

    @tps_check_res.setter
    def tps_check_res(self, tps_check_res):
        """Sets the tps_check_res of this CaseReportDetail.

        TPS检查结果

        :param tps_check_res: The tps_check_res of this CaseReportDetail.
        :type tps_check_res: bool
        """
        self._tps_check_res = tps_check_res

    @property
    def tran_tps(self):
        """Gets the tran_tps of this CaseReportDetail.

        平均TPS

        :return: The tran_tps of this CaseReportDetail.
        :rtype: float
        """
        return self._tran_tps

    @tran_tps.setter
    def tran_tps(self, tran_tps):
        """Sets the tran_tps of this CaseReportDetail.

        平均TPS

        :param tran_tps: The tran_tps of this CaseReportDetail.
        :type tran_tps: float
        """
        self._tran_tps = tran_tps

    @property
    def tran_tps_check_point(self):
        """Gets the tran_tps_check_point of this CaseReportDetail.

        平均TPS检查点

        :return: The tran_tps_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._tran_tps_check_point

    @tran_tps_check_point.setter
    def tran_tps_check_point(self, tran_tps_check_point):
        """Sets the tran_tps_check_point of this CaseReportDetail.

        平均TPS检查点

        :param tran_tps_check_point: The tran_tps_check_point of this CaseReportDetail.
        :type tran_tps_check_point: float
        """
        self._tran_tps_check_point = tran_tps_check_point

    @property
    def tran_tps_check_res(self):
        """Gets the tran_tps_check_res of this CaseReportDetail.

        平均TPS检查结果

        :return: The tran_tps_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._tran_tps_check_res

    @tran_tps_check_res.setter
    def tran_tps_check_res(self, tran_tps_check_res):
        """Sets the tran_tps_check_res of this CaseReportDetail.

        平均TPS检查结果

        :param tran_tps_check_res: The tran_tps_check_res of this CaseReportDetail.
        :type tran_tps_check_res: bool
        """
        self._tran_tps_check_res = tran_tps_check_res

    @property
    def transaction_id(self):
        """Gets the transaction_id of this CaseReportDetail.

        事务ID

        :return: The transaction_id of this CaseReportDetail.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this CaseReportDetail.

        事务ID

        :param transaction_id: The transaction_id of this CaseReportDetail.
        :type transaction_id: str
        """
        self._transaction_id = transaction_id

    @property
    def transaction_success(self):
        """Gets the transaction_success of this CaseReportDetail.

        事务成功数

        :return: The transaction_success of this CaseReportDetail.
        :rtype: float
        """
        return self._transaction_success

    @transaction_success.setter
    def transaction_success(self, transaction_success):
        """Sets the transaction_success of this CaseReportDetail.

        事务成功数

        :param transaction_success: The transaction_success of this CaseReportDetail.
        :type transaction_success: float
        """
        self._transaction_success = transaction_success

    @property
    def transactions(self):
        """Gets the transactions of this CaseReportDetail.

        事务数

        :return: The transactions of this CaseReportDetail.
        :rtype: float
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this CaseReportDetail.

        事务数

        :param transactions: The transactions of this CaseReportDetail.
        :type transactions: float
        """
        self._transactions = transactions

    @property
    def transactions_check_point(self):
        """Gets the transactions_check_point of this CaseReportDetail.

        事务数检查点

        :return: The transactions_check_point of this CaseReportDetail.
        :rtype: float
        """
        return self._transactions_check_point

    @transactions_check_point.setter
    def transactions_check_point(self, transactions_check_point):
        """Sets the transactions_check_point of this CaseReportDetail.

        事务数检查点

        :param transactions_check_point: The transactions_check_point of this CaseReportDetail.
        :type transactions_check_point: float
        """
        self._transactions_check_point = transactions_check_point

    @property
    def transactions_check_res(self):
        """Gets the transactions_check_res of this CaseReportDetail.

        事务数检查结果

        :return: The transactions_check_res of this CaseReportDetail.
        :rtype: bool
        """
        return self._transactions_check_res

    @transactions_check_res.setter
    def transactions_check_res(self, transactions_check_res):
        """Sets the transactions_check_res of this CaseReportDetail.

        事务数检查结果

        :param transactions_check_res: The transactions_check_res of this CaseReportDetail.
        :type transactions_check_res: bool
        """
        self._transactions_check_res = transactions_check_res

    @property
    def update_time(self):
        """Gets the update_time of this CaseReportDetail.

        更新时间

        :return: The update_time of this CaseReportDetail.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this CaseReportDetail.

        更新时间

        :param update_time: The update_time of this CaseReportDetail.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def url(self):
        """Gets the url of this CaseReportDetail.

        aw的http url

        :return: The url of this CaseReportDetail.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CaseReportDetail.

        aw的http url

        :param url: The url of this CaseReportDetail.
        :type url: str
        """
        self._url = url

    @property
    def user_concur(self):
        """Gets the user_concur of this CaseReportDetail.

        反应实时vuser数据

        :return: The user_concur of this CaseReportDetail.
        :rtype: int
        """
        return self._user_concur

    @user_concur.setter
    def user_concur(self, user_concur):
        """Sets the user_concur of this CaseReportDetail.

        反应实时vuser数据

        :param user_concur: The user_concur of this CaseReportDetail.
        :type user_concur: int
        """
        self._user_concur = user_concur

    @property
    def version_uri(self):
        """Gets the version_uri of this CaseReportDetail.

        分支uri

        :return: The version_uri of this CaseReportDetail.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        """Sets the version_uri of this CaseReportDetail.

        分支uri

        :param version_uri: The version_uri of this CaseReportDetail.
        :type version_uri: str
        """
        self._version_uri = version_uri

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CaseReportDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
