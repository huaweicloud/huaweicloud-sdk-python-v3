# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTopTableVolumesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_volumes': 'list[TableVolumeResult]',
        'total_count': 'int',
        'state': 'str'
    }

    attribute_map = {
        'table_volumes': 'table_volumes',
        'total_count': 'total_count',
        'state': 'state'
    }

    def __init__(self, table_volumes=None, total_count=None, state=None):
        r"""ListTopTableVolumesResponse

        The model defined in huaweicloud sdk

        :param table_volumes: **参数解释**: 数据库表占用空间列表。 
        :type table_volumes: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.TableVolumeResult`]
        :param total_count: **参数解释**: 总数。 **取值范围**: 不涉及。 
        :type total_count: int
        :param state: **参数解释**: 任务状态。 **取值范围**: - RUNNING：运行中。 - ERROR：运行异常。 - FINISHED： 运行结束。 
        :type state: str
        """
        
        super().__init__()

        self._table_volumes = None
        self._total_count = None
        self._state = None
        self.discriminator = None

        if table_volumes is not None:
            self.table_volumes = table_volumes
        if total_count is not None:
            self.total_count = total_count
        if state is not None:
            self.state = state

    @property
    def table_volumes(self):
        r"""Gets the table_volumes of this ListTopTableVolumesResponse.

        **参数解释**: 数据库表占用空间列表。 

        :return: The table_volumes of this ListTopTableVolumesResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.TableVolumeResult`]
        """
        return self._table_volumes

    @table_volumes.setter
    def table_volumes(self, table_volumes):
        r"""Sets the table_volumes of this ListTopTableVolumesResponse.

        **参数解释**: 数据库表占用空间列表。 

        :param table_volumes: The table_volumes of this ListTopTableVolumesResponse.
        :type table_volumes: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.TableVolumeResult`]
        """
        self._table_volumes = table_volumes

    @property
    def total_count(self):
        r"""Gets the total_count of this ListTopTableVolumesResponse.

        **参数解释**: 总数。 **取值范围**: 不涉及。 

        :return: The total_count of this ListTopTableVolumesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListTopTableVolumesResponse.

        **参数解释**: 总数。 **取值范围**: 不涉及。 

        :param total_count: The total_count of this ListTopTableVolumesResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def state(self):
        r"""Gets the state of this ListTopTableVolumesResponse.

        **参数解释**: 任务状态。 **取值范围**: - RUNNING：运行中。 - ERROR：运行异常。 - FINISHED： 运行结束。 

        :return: The state of this ListTopTableVolumesResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListTopTableVolumesResponse.

        **参数解释**: 任务状态。 **取值范围**: - RUNNING：运行中。 - ERROR：运行异常。 - FINISHED： 运行结束。 

        :param state: The state of this ListTopTableVolumesResponse.
        :type state: str
        """
        self._state = state

    def to_dict(self):
        import warnings
        warnings.warn("ListTopTableVolumesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListTopTableVolumesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
