# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssetTaskInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'asset_id': 'str',
        'create_time_after': 'str',
        'create_time_before': 'str',
        'end_time_after': 'str',
        'end_time_before': 'str',
        'status': 'list[str]',
        'marker': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'type': 'type',
        'asset_id': 'asset_id',
        'create_time_after': 'create_time_after',
        'create_time_before': 'create_time_before',
        'end_time_after': 'end_time_after',
        'end_time_before': 'end_time_before',
        'status': 'status',
        'marker': 'marker',
        'limit': 'limit'
    }

    def __init__(self, type=None, asset_id=None, create_time_after=None, create_time_before=None, end_time_after=None, end_time_before=None, status=None, marker=None, limit=None):
        r"""ListAssetTaskInfoRequest

        The model defined in huaweicloud sdk

        :param type: 任务类型
        :type type: str
        :param asset_id: 媒资Id
        :type asset_id: str
        :param create_time_after: 根据任务创建时间匹配该时间之后的，包含该时间点，格式按照RFC3339，UTC时间，如2020-09-01T18:50:20Z
        :type create_time_after: str
        :param create_time_before: 根据任务创建时间匹配该时间之前的，不包含该时间点，格式按照RFC3339，UTC时间，如2020-09-01T18:50:20Z
        :type create_time_before: str
        :param end_time_after: 根据任务结束时间匹配该时间之后的，包含该时间点，格式按照RFC3339，UTC时间，如2020-09-01T18:50:20Z
        :type end_time_after: str
        :param end_time_before: 根据任务结束时间匹配该时间之前的，不包含该时间点，格式按照RFC3339，UTC时间，如2020-09-01T18:50:20Z
        :type end_time_before: str
        :param status: 任务状态
        :type status: list[str]
        :param marker: 标志位，不传默认表示从第一条开始
        :type marker: str
        :param limit: 返回的每页个数，默认10，最大100，最小1
        :type limit: int
        """
        
        

        self._type = None
        self._asset_id = None
        self._create_time_after = None
        self._create_time_before = None
        self._end_time_after = None
        self._end_time_before = None
        self._status = None
        self._marker = None
        self._limit = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if asset_id is not None:
            self.asset_id = asset_id
        if create_time_after is not None:
            self.create_time_after = create_time_after
        if create_time_before is not None:
            self.create_time_before = create_time_before
        if end_time_after is not None:
            self.end_time_after = end_time_after
        if end_time_before is not None:
            self.end_time_before = end_time_before
        if status is not None:
            self.status = status
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit

    @property
    def type(self):
        r"""Gets the type of this ListAssetTaskInfoRequest.

        任务类型

        :return: The type of this ListAssetTaskInfoRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListAssetTaskInfoRequest.

        任务类型

        :param type: The type of this ListAssetTaskInfoRequest.
        :type type: str
        """
        self._type = type

    @property
    def asset_id(self):
        r"""Gets the asset_id of this ListAssetTaskInfoRequest.

        媒资Id

        :return: The asset_id of this ListAssetTaskInfoRequest.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this ListAssetTaskInfoRequest.

        媒资Id

        :param asset_id: The asset_id of this ListAssetTaskInfoRequest.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def create_time_after(self):
        r"""Gets the create_time_after of this ListAssetTaskInfoRequest.

        根据任务创建时间匹配该时间之后的，包含该时间点，格式按照RFC3339，UTC时间，如2020-09-01T18:50:20Z

        :return: The create_time_after of this ListAssetTaskInfoRequest.
        :rtype: str
        """
        return self._create_time_after

    @create_time_after.setter
    def create_time_after(self, create_time_after):
        r"""Sets the create_time_after of this ListAssetTaskInfoRequest.

        根据任务创建时间匹配该时间之后的，包含该时间点，格式按照RFC3339，UTC时间，如2020-09-01T18:50:20Z

        :param create_time_after: The create_time_after of this ListAssetTaskInfoRequest.
        :type create_time_after: str
        """
        self._create_time_after = create_time_after

    @property
    def create_time_before(self):
        r"""Gets the create_time_before of this ListAssetTaskInfoRequest.

        根据任务创建时间匹配该时间之前的，不包含该时间点，格式按照RFC3339，UTC时间，如2020-09-01T18:50:20Z

        :return: The create_time_before of this ListAssetTaskInfoRequest.
        :rtype: str
        """
        return self._create_time_before

    @create_time_before.setter
    def create_time_before(self, create_time_before):
        r"""Sets the create_time_before of this ListAssetTaskInfoRequest.

        根据任务创建时间匹配该时间之前的，不包含该时间点，格式按照RFC3339，UTC时间，如2020-09-01T18:50:20Z

        :param create_time_before: The create_time_before of this ListAssetTaskInfoRequest.
        :type create_time_before: str
        """
        self._create_time_before = create_time_before

    @property
    def end_time_after(self):
        r"""Gets the end_time_after of this ListAssetTaskInfoRequest.

        根据任务结束时间匹配该时间之后的，包含该时间点，格式按照RFC3339，UTC时间，如2020-09-01T18:50:20Z

        :return: The end_time_after of this ListAssetTaskInfoRequest.
        :rtype: str
        """
        return self._end_time_after

    @end_time_after.setter
    def end_time_after(self, end_time_after):
        r"""Sets the end_time_after of this ListAssetTaskInfoRequest.

        根据任务结束时间匹配该时间之后的，包含该时间点，格式按照RFC3339，UTC时间，如2020-09-01T18:50:20Z

        :param end_time_after: The end_time_after of this ListAssetTaskInfoRequest.
        :type end_time_after: str
        """
        self._end_time_after = end_time_after

    @property
    def end_time_before(self):
        r"""Gets the end_time_before of this ListAssetTaskInfoRequest.

        根据任务结束时间匹配该时间之前的，不包含该时间点，格式按照RFC3339，UTC时间，如2020-09-01T18:50:20Z

        :return: The end_time_before of this ListAssetTaskInfoRequest.
        :rtype: str
        """
        return self._end_time_before

    @end_time_before.setter
    def end_time_before(self, end_time_before):
        r"""Sets the end_time_before of this ListAssetTaskInfoRequest.

        根据任务结束时间匹配该时间之前的，不包含该时间点，格式按照RFC3339，UTC时间，如2020-09-01T18:50:20Z

        :param end_time_before: The end_time_before of this ListAssetTaskInfoRequest.
        :type end_time_before: str
        """
        self._end_time_before = end_time_before

    @property
    def status(self):
        r"""Gets the status of this ListAssetTaskInfoRequest.

        任务状态

        :return: The status of this ListAssetTaskInfoRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListAssetTaskInfoRequest.

        任务状态

        :param status: The status of this ListAssetTaskInfoRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def marker(self):
        r"""Gets the marker of this ListAssetTaskInfoRequest.

        标志位，不传默认表示从第一条开始

        :return: The marker of this ListAssetTaskInfoRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListAssetTaskInfoRequest.

        标志位，不传默认表示从第一条开始

        :param marker: The marker of this ListAssetTaskInfoRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListAssetTaskInfoRequest.

        返回的每页个数，默认10，最大100，最小1

        :return: The limit of this ListAssetTaskInfoRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAssetTaskInfoRequest.

        返回的每页个数，默认10，最大100，最小1

        :param limit: The limit of this ListAssetTaskInfoRequest.
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
        if not isinstance(other, ListAssetTaskInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
