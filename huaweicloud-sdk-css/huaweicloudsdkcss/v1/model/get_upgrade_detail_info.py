# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetUpgradeDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'agency_name': 'str',
        'image_info': 'GetTargetImageIdDetail',
        'total_nodes': 'str',
        'completed_nodes': 'str',
        'current_node_name': 'str',
        'execute_times': 'str',
        'migrate_param': 'str',
        'final_az_info_map': 'str',
        'current_node_detail': 'list[CurrentNodeDetail]'
    }

    attribute_map = {
        'id': 'id',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'status': 'status',
        'agency_name': 'agencyName',
        'image_info': 'imageInfo',
        'total_nodes': 'totalNodes',
        'completed_nodes': 'completedNodes',
        'current_node_name': 'currentNodeName',
        'execute_times': 'executeTimes',
        'migrate_param': 'migrateParam',
        'final_az_info_map': 'finalAzInfoMap',
        'current_node_detail': 'currentNodeDetail'
    }

    def __init__(self, id=None, start_time=None, end_time=None, status=None, agency_name=None, image_info=None, total_nodes=None, completed_nodes=None, current_node_name=None, execute_times=None, migrate_param=None, final_az_info_map=None, current_node_detail=None):
        r"""GetUpgradeDetailInfo

        The model defined in huaweicloud sdk

        :param id: 任务ID。
        :type id: str
        :param start_time: 升级开始时间。
        :type start_time: str
        :param end_time: 升级结束时间。
        :type end_time: str
        :param status: 任务状态。 - RUNNING：升级中。 - SUCCESS：升级成功。 - FAILED：升级失败。 - PARTIAL_FAILED：部分升级失败。
        :type status: str
        :param agency_name: 委托名称，委托给CSS，允许CSS调用您的其他云服务。
        :type agency_name: str
        :param image_info: 
        :type image_info: :class:`huaweicloudsdkcss.v1.GetTargetImageIdDetail`
        :param total_nodes: 所有需要升级的节点名称集合。
        :type total_nodes: str
        :param completed_nodes: 所有升级完成的节点名称集合。
        :type completed_nodes: str
        :param current_node_name: 当前正在升级的节点名称。
        :type current_node_name: str
        :param execute_times: 重试次数。
        :type execute_times: str
        :param migrate_param: 集群当前升级的行为。当有query参数时显示该返回值。
        :type migrate_param: str
        :param final_az_info_map: 集群升级预期结果。当有query参数时显示该返回值。
        :type final_az_info_map: str
        :param current_node_detail: 
        :type current_node_detail: list[:class:`huaweicloudsdkcss.v1.CurrentNodeDetail`]
        """
        
        

        self._id = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self._agency_name = None
        self._image_info = None
        self._total_nodes = None
        self._completed_nodes = None
        self._current_node_name = None
        self._execute_times = None
        self._migrate_param = None
        self._final_az_info_map = None
        self._current_node_detail = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if agency_name is not None:
            self.agency_name = agency_name
        if image_info is not None:
            self.image_info = image_info
        if total_nodes is not None:
            self.total_nodes = total_nodes
        if completed_nodes is not None:
            self.completed_nodes = completed_nodes
        if current_node_name is not None:
            self.current_node_name = current_node_name
        if execute_times is not None:
            self.execute_times = execute_times
        if migrate_param is not None:
            self.migrate_param = migrate_param
        if final_az_info_map is not None:
            self.final_az_info_map = final_az_info_map
        if current_node_detail is not None:
            self.current_node_detail = current_node_detail

    @property
    def id(self):
        r"""Gets the id of this GetUpgradeDetailInfo.

        任务ID。

        :return: The id of this GetUpgradeDetailInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GetUpgradeDetailInfo.

        任务ID。

        :param id: The id of this GetUpgradeDetailInfo.
        :type id: str
        """
        self._id = id

    @property
    def start_time(self):
        r"""Gets the start_time of this GetUpgradeDetailInfo.

        升级开始时间。

        :return: The start_time of this GetUpgradeDetailInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this GetUpgradeDetailInfo.

        升级开始时间。

        :param start_time: The start_time of this GetUpgradeDetailInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this GetUpgradeDetailInfo.

        升级结束时间。

        :return: The end_time of this GetUpgradeDetailInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this GetUpgradeDetailInfo.

        升级结束时间。

        :param end_time: The end_time of this GetUpgradeDetailInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        r"""Gets the status of this GetUpgradeDetailInfo.

        任务状态。 - RUNNING：升级中。 - SUCCESS：升级成功。 - FAILED：升级失败。 - PARTIAL_FAILED：部分升级失败。

        :return: The status of this GetUpgradeDetailInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this GetUpgradeDetailInfo.

        任务状态。 - RUNNING：升级中。 - SUCCESS：升级成功。 - FAILED：升级失败。 - PARTIAL_FAILED：部分升级失败。

        :param status: The status of this GetUpgradeDetailInfo.
        :type status: str
        """
        self._status = status

    @property
    def agency_name(self):
        r"""Gets the agency_name of this GetUpgradeDetailInfo.

        委托名称，委托给CSS，允许CSS调用您的其他云服务。

        :return: The agency_name of this GetUpgradeDetailInfo.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this GetUpgradeDetailInfo.

        委托名称，委托给CSS，允许CSS调用您的其他云服务。

        :param agency_name: The agency_name of this GetUpgradeDetailInfo.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def image_info(self):
        r"""Gets the image_info of this GetUpgradeDetailInfo.

        :return: The image_info of this GetUpgradeDetailInfo.
        :rtype: :class:`huaweicloudsdkcss.v1.GetTargetImageIdDetail`
        """
        return self._image_info

    @image_info.setter
    def image_info(self, image_info):
        r"""Sets the image_info of this GetUpgradeDetailInfo.

        :param image_info: The image_info of this GetUpgradeDetailInfo.
        :type image_info: :class:`huaweicloudsdkcss.v1.GetTargetImageIdDetail`
        """
        self._image_info = image_info

    @property
    def total_nodes(self):
        r"""Gets the total_nodes of this GetUpgradeDetailInfo.

        所有需要升级的节点名称集合。

        :return: The total_nodes of this GetUpgradeDetailInfo.
        :rtype: str
        """
        return self._total_nodes

    @total_nodes.setter
    def total_nodes(self, total_nodes):
        r"""Sets the total_nodes of this GetUpgradeDetailInfo.

        所有需要升级的节点名称集合。

        :param total_nodes: The total_nodes of this GetUpgradeDetailInfo.
        :type total_nodes: str
        """
        self._total_nodes = total_nodes

    @property
    def completed_nodes(self):
        r"""Gets the completed_nodes of this GetUpgradeDetailInfo.

        所有升级完成的节点名称集合。

        :return: The completed_nodes of this GetUpgradeDetailInfo.
        :rtype: str
        """
        return self._completed_nodes

    @completed_nodes.setter
    def completed_nodes(self, completed_nodes):
        r"""Sets the completed_nodes of this GetUpgradeDetailInfo.

        所有升级完成的节点名称集合。

        :param completed_nodes: The completed_nodes of this GetUpgradeDetailInfo.
        :type completed_nodes: str
        """
        self._completed_nodes = completed_nodes

    @property
    def current_node_name(self):
        r"""Gets the current_node_name of this GetUpgradeDetailInfo.

        当前正在升级的节点名称。

        :return: The current_node_name of this GetUpgradeDetailInfo.
        :rtype: str
        """
        return self._current_node_name

    @current_node_name.setter
    def current_node_name(self, current_node_name):
        r"""Sets the current_node_name of this GetUpgradeDetailInfo.

        当前正在升级的节点名称。

        :param current_node_name: The current_node_name of this GetUpgradeDetailInfo.
        :type current_node_name: str
        """
        self._current_node_name = current_node_name

    @property
    def execute_times(self):
        r"""Gets the execute_times of this GetUpgradeDetailInfo.

        重试次数。

        :return: The execute_times of this GetUpgradeDetailInfo.
        :rtype: str
        """
        return self._execute_times

    @execute_times.setter
    def execute_times(self, execute_times):
        r"""Sets the execute_times of this GetUpgradeDetailInfo.

        重试次数。

        :param execute_times: The execute_times of this GetUpgradeDetailInfo.
        :type execute_times: str
        """
        self._execute_times = execute_times

    @property
    def migrate_param(self):
        r"""Gets the migrate_param of this GetUpgradeDetailInfo.

        集群当前升级的行为。当有query参数时显示该返回值。

        :return: The migrate_param of this GetUpgradeDetailInfo.
        :rtype: str
        """
        return self._migrate_param

    @migrate_param.setter
    def migrate_param(self, migrate_param):
        r"""Sets the migrate_param of this GetUpgradeDetailInfo.

        集群当前升级的行为。当有query参数时显示该返回值。

        :param migrate_param: The migrate_param of this GetUpgradeDetailInfo.
        :type migrate_param: str
        """
        self._migrate_param = migrate_param

    @property
    def final_az_info_map(self):
        r"""Gets the final_az_info_map of this GetUpgradeDetailInfo.

        集群升级预期结果。当有query参数时显示该返回值。

        :return: The final_az_info_map of this GetUpgradeDetailInfo.
        :rtype: str
        """
        return self._final_az_info_map

    @final_az_info_map.setter
    def final_az_info_map(self, final_az_info_map):
        r"""Sets the final_az_info_map of this GetUpgradeDetailInfo.

        集群升级预期结果。当有query参数时显示该返回值。

        :param final_az_info_map: The final_az_info_map of this GetUpgradeDetailInfo.
        :type final_az_info_map: str
        """
        self._final_az_info_map = final_az_info_map

    @property
    def current_node_detail(self):
        r"""Gets the current_node_detail of this GetUpgradeDetailInfo.

        :return: The current_node_detail of this GetUpgradeDetailInfo.
        :rtype: list[:class:`huaweicloudsdkcss.v1.CurrentNodeDetail`]
        """
        return self._current_node_detail

    @current_node_detail.setter
    def current_node_detail(self, current_node_detail):
        r"""Sets the current_node_detail of this GetUpgradeDetailInfo.

        :param current_node_detail: The current_node_detail of this GetUpgradeDetailInfo.
        :type current_node_detail: list[:class:`huaweicloudsdkcss.v1.CurrentNodeDetail`]
        """
        self._current_node_detail = current_node_detail

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
        if not isinstance(other, GetUpgradeDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
