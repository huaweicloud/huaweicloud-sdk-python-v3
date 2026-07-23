# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobSchedulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schedule_type': 'str',
        'schedule_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'schedule_type': 'schedule_type',
        'schedule_id': 'schedule_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, schedule_type=None, schedule_id=None, offset=None, limit=None):
        r"""ListJobSchedulesRequest

        The model defined in huaweicloud sdk

        :param schedule_type: 策略类型，snapshot:快照策略, sync:同步策略，默认查询所有类型
        :type schedule_type: str
        :param schedule_id: 策略id
        :type schedule_id: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。默认为10，不能为负数，最小值为1，最大值为200。
        :type limit: int
        """
        
        

        self._schedule_type = None
        self._schedule_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if schedule_type is not None:
            self.schedule_type = schedule_type
        if schedule_id is not None:
            self.schedule_id = schedule_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def schedule_type(self):
        r"""Gets the schedule_type of this ListJobSchedulesRequest.

        策略类型，snapshot:快照策略, sync:同步策略，默认查询所有类型

        :return: The schedule_type of this ListJobSchedulesRequest.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        r"""Sets the schedule_type of this ListJobSchedulesRequest.

        策略类型，snapshot:快照策略, sync:同步策略，默认查询所有类型

        :param schedule_type: The schedule_type of this ListJobSchedulesRequest.
        :type schedule_type: str
        """
        self._schedule_type = schedule_type

    @property
    def schedule_id(self):
        r"""Gets the schedule_id of this ListJobSchedulesRequest.

        策略id

        :return: The schedule_id of this ListJobSchedulesRequest.
        :rtype: str
        """
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, schedule_id):
        r"""Sets the schedule_id of this ListJobSchedulesRequest.

        策略id

        :param schedule_id: The schedule_id of this ListJobSchedulesRequest.
        :type schedule_id: str
        """
        self._schedule_id = schedule_id

    @property
    def offset(self):
        r"""Gets the offset of this ListJobSchedulesRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListJobSchedulesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListJobSchedulesRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListJobSchedulesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListJobSchedulesRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为200。

        :return: The limit of this ListJobSchedulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListJobSchedulesRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为200。

        :param limit: The limit of this ListJobSchedulesRequest.
        :type limit: int
        """
        self._limit = limit

    def to_dict(self):
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
        if not isinstance(other, ListJobSchedulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
