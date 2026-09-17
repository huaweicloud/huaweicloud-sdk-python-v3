# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceEmergencyLogsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'data': 'list[DDSEmergencyLogInfo]',
        'object_type': 'str',
        'collect_date': 'str'
    }

    attribute_map = {
        'total': 'total',
        'data': 'data',
        'object_type': 'object_type',
        'collect_date': 'collect_date'
    }

    def __init__(self, total=None, data=None, object_type=None, collect_date=None):
        r"""ListInstanceEmergencyLogsResponse

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param data: 数据列表
        :type data: list[:class:`huaweicloudsdkdas.v3.DDSEmergencyLogInfo`]
        :param object_type: 对象类型
        :type object_type: str
        :param collect_date: 采集时间
        :type collect_date: str
        """
        
        super().__init__()

        self._total = None
        self._data = None
        self._object_type = None
        self._collect_date = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if data is not None:
            self.data = data
        if object_type is not None:
            self.object_type = object_type
        if collect_date is not None:
            self.collect_date = collect_date

    @property
    def total(self):
        r"""Gets the total of this ListInstanceEmergencyLogsResponse.

        总数

        :return: The total of this ListInstanceEmergencyLogsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListInstanceEmergencyLogsResponse.

        总数

        :param total: The total of this ListInstanceEmergencyLogsResponse.
        :type total: int
        """
        self._total = total

    @property
    def data(self):
        r"""Gets the data of this ListInstanceEmergencyLogsResponse.

        数据列表

        :return: The data of this ListInstanceEmergencyLogsResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.DDSEmergencyLogInfo`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListInstanceEmergencyLogsResponse.

        数据列表

        :param data: The data of this ListInstanceEmergencyLogsResponse.
        :type data: list[:class:`huaweicloudsdkdas.v3.DDSEmergencyLogInfo`]
        """
        self._data = data

    @property
    def object_type(self):
        r"""Gets the object_type of this ListInstanceEmergencyLogsResponse.

        对象类型

        :return: The object_type of this ListInstanceEmergencyLogsResponse.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this ListInstanceEmergencyLogsResponse.

        对象类型

        :param object_type: The object_type of this ListInstanceEmergencyLogsResponse.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def collect_date(self):
        r"""Gets the collect_date of this ListInstanceEmergencyLogsResponse.

        采集时间

        :return: The collect_date of this ListInstanceEmergencyLogsResponse.
        :rtype: str
        """
        return self._collect_date

    @collect_date.setter
    def collect_date(self, collect_date):
        r"""Sets the collect_date of this ListInstanceEmergencyLogsResponse.

        采集时间

        :param collect_date: The collect_date of this ListInstanceEmergencyLogsResponse.
        :type collect_date: str
        """
        self._collect_date = collect_date

    def to_dict(self):
        import warnings
        warnings.warn("ListInstanceEmergencyLogsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListInstanceEmergencyLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
