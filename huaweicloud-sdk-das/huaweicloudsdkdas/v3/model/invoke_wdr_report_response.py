# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InvokeWdrReportResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_wdr': 'str',
        'instance_wdr_name': 'str',
        'node_wdr_list': 'list[NodeWdrDto]',
        'wdr_status': 'int',
        'start_snapshot_id': 'int',
        'end_snapshot_id': 'int'
    }

    attribute_map = {
        'instance_wdr': 'instance_wdr',
        'instance_wdr_name': 'instance_wdr_name',
        'node_wdr_list': 'node_wdr_list',
        'wdr_status': 'wdr_status',
        'start_snapshot_id': 'start_snapshot_id',
        'end_snapshot_id': 'end_snapshot_id'
    }

    def __init__(self, instance_wdr=None, instance_wdr_name=None, node_wdr_list=None, wdr_status=None, start_snapshot_id=None, end_snapshot_id=None):
        r"""InvokeWdrReportResponse

        The model defined in huaweicloud sdk

        :param instance_wdr: 实例WDR报表下载地址
        :type instance_wdr: str
        :param instance_wdr_name: WDR报表名称
        :type instance_wdr_name: str
        :param node_wdr_list: 节点WDR报表列表
        :type node_wdr_list: list[:class:`huaweicloudsdkdas.v3.NodeWdrDto`]
        :param wdr_status: WDR报表状态。取值范围：0（无报表）、1（生成中）、2（生成成功）、3（生成失败）
        :type wdr_status: int
        :param start_snapshot_id: WDR快照开始ID
        :type start_snapshot_id: int
        :param end_snapshot_id: WDR快照结束ID
        :type end_snapshot_id: int
        """
        
        super().__init__()

        self._instance_wdr = None
        self._instance_wdr_name = None
        self._node_wdr_list = None
        self._wdr_status = None
        self._start_snapshot_id = None
        self._end_snapshot_id = None
        self.discriminator = None

        if instance_wdr is not None:
            self.instance_wdr = instance_wdr
        if instance_wdr_name is not None:
            self.instance_wdr_name = instance_wdr_name
        if node_wdr_list is not None:
            self.node_wdr_list = node_wdr_list
        if wdr_status is not None:
            self.wdr_status = wdr_status
        if start_snapshot_id is not None:
            self.start_snapshot_id = start_snapshot_id
        if end_snapshot_id is not None:
            self.end_snapshot_id = end_snapshot_id

    @property
    def instance_wdr(self):
        r"""Gets the instance_wdr of this InvokeWdrReportResponse.

        实例WDR报表下载地址

        :return: The instance_wdr of this InvokeWdrReportResponse.
        :rtype: str
        """
        return self._instance_wdr

    @instance_wdr.setter
    def instance_wdr(self, instance_wdr):
        r"""Sets the instance_wdr of this InvokeWdrReportResponse.

        实例WDR报表下载地址

        :param instance_wdr: The instance_wdr of this InvokeWdrReportResponse.
        :type instance_wdr: str
        """
        self._instance_wdr = instance_wdr

    @property
    def instance_wdr_name(self):
        r"""Gets the instance_wdr_name of this InvokeWdrReportResponse.

        WDR报表名称

        :return: The instance_wdr_name of this InvokeWdrReportResponse.
        :rtype: str
        """
        return self._instance_wdr_name

    @instance_wdr_name.setter
    def instance_wdr_name(self, instance_wdr_name):
        r"""Sets the instance_wdr_name of this InvokeWdrReportResponse.

        WDR报表名称

        :param instance_wdr_name: The instance_wdr_name of this InvokeWdrReportResponse.
        :type instance_wdr_name: str
        """
        self._instance_wdr_name = instance_wdr_name

    @property
    def node_wdr_list(self):
        r"""Gets the node_wdr_list of this InvokeWdrReportResponse.

        节点WDR报表列表

        :return: The node_wdr_list of this InvokeWdrReportResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.NodeWdrDto`]
        """
        return self._node_wdr_list

    @node_wdr_list.setter
    def node_wdr_list(self, node_wdr_list):
        r"""Sets the node_wdr_list of this InvokeWdrReportResponse.

        节点WDR报表列表

        :param node_wdr_list: The node_wdr_list of this InvokeWdrReportResponse.
        :type node_wdr_list: list[:class:`huaweicloudsdkdas.v3.NodeWdrDto`]
        """
        self._node_wdr_list = node_wdr_list

    @property
    def wdr_status(self):
        r"""Gets the wdr_status of this InvokeWdrReportResponse.

        WDR报表状态。取值范围：0（无报表）、1（生成中）、2（生成成功）、3（生成失败）

        :return: The wdr_status of this InvokeWdrReportResponse.
        :rtype: int
        """
        return self._wdr_status

    @wdr_status.setter
    def wdr_status(self, wdr_status):
        r"""Sets the wdr_status of this InvokeWdrReportResponse.

        WDR报表状态。取值范围：0（无报表）、1（生成中）、2（生成成功）、3（生成失败）

        :param wdr_status: The wdr_status of this InvokeWdrReportResponse.
        :type wdr_status: int
        """
        self._wdr_status = wdr_status

    @property
    def start_snapshot_id(self):
        r"""Gets the start_snapshot_id of this InvokeWdrReportResponse.

        WDR快照开始ID

        :return: The start_snapshot_id of this InvokeWdrReportResponse.
        :rtype: int
        """
        return self._start_snapshot_id

    @start_snapshot_id.setter
    def start_snapshot_id(self, start_snapshot_id):
        r"""Sets the start_snapshot_id of this InvokeWdrReportResponse.

        WDR快照开始ID

        :param start_snapshot_id: The start_snapshot_id of this InvokeWdrReportResponse.
        :type start_snapshot_id: int
        """
        self._start_snapshot_id = start_snapshot_id

    @property
    def end_snapshot_id(self):
        r"""Gets the end_snapshot_id of this InvokeWdrReportResponse.

        WDR快照结束ID

        :return: The end_snapshot_id of this InvokeWdrReportResponse.
        :rtype: int
        """
        return self._end_snapshot_id

    @end_snapshot_id.setter
    def end_snapshot_id(self, end_snapshot_id):
        r"""Sets the end_snapshot_id of this InvokeWdrReportResponse.

        WDR快照结束ID

        :param end_snapshot_id: The end_snapshot_id of this InvokeWdrReportResponse.
        :type end_snapshot_id: int
        """
        self._end_snapshot_id = end_snapshot_id

    def to_dict(self):
        import warnings
        warnings.warn("InvokeWdrReportResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InvokeWdrReportResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
