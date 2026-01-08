# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Result:

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
        'status': 'str',
        'create_time': 'str',
        'end_time': 'str',
        'transcode_result': 'TranscodeInfoResult'
    }

    attribute_map = {
        'type': 'type',
        'asset_id': 'asset_id',
        'status': 'status',
        'create_time': 'create_time',
        'end_time': 'end_time',
        'transcode_result': 'transcode_result'
    }

    def __init__(self, type=None, asset_id=None, status=None, create_time=None, end_time=None, transcode_result=None):
        r"""Result

        The model defined in huaweicloud sdk

        :param type: 任务类型 
        :type type: str
        :param asset_id: 媒资ID 
        :type asset_id: str
        :param status: 转码状态 - WAITING 等待中 - PROCESSING 处理中 - SUCCEED 成功 - FAILED 失败 
        :type status: str
        :param create_time: 转码下发时间，格式按照RFC3339，UTC时间 
        :type create_time: str
        :param end_time: 转码结束时间 
        :type end_time: str
        :param transcode_result: 
        :type transcode_result: :class:`huaweicloudsdkvod.v1.TranscodeInfoResult`
        """
        
        

        self._type = None
        self._asset_id = None
        self._status = None
        self._create_time = None
        self._end_time = None
        self._transcode_result = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if asset_id is not None:
            self.asset_id = asset_id
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if end_time is not None:
            self.end_time = end_time
        if transcode_result is not None:
            self.transcode_result = transcode_result

    @property
    def type(self):
        r"""Gets the type of this Result.

        任务类型 

        :return: The type of this Result.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Result.

        任务类型 

        :param type: The type of this Result.
        :type type: str
        """
        self._type = type

    @property
    def asset_id(self):
        r"""Gets the asset_id of this Result.

        媒资ID 

        :return: The asset_id of this Result.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this Result.

        媒资ID 

        :param asset_id: The asset_id of this Result.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def status(self):
        r"""Gets the status of this Result.

        转码状态 - WAITING 等待中 - PROCESSING 处理中 - SUCCEED 成功 - FAILED 失败 

        :return: The status of this Result.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Result.

        转码状态 - WAITING 等待中 - PROCESSING 处理中 - SUCCEED 成功 - FAILED 失败 

        :param status: The status of this Result.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this Result.

        转码下发时间，格式按照RFC3339，UTC时间 

        :return: The create_time of this Result.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this Result.

        转码下发时间，格式按照RFC3339，UTC时间 

        :param create_time: The create_time of this Result.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def end_time(self):
        r"""Gets the end_time of this Result.

        转码结束时间 

        :return: The end_time of this Result.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this Result.

        转码结束时间 

        :param end_time: The end_time of this Result.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def transcode_result(self):
        r"""Gets the transcode_result of this Result.

        :return: The transcode_result of this Result.
        :rtype: :class:`huaweicloudsdkvod.v1.TranscodeInfoResult`
        """
        return self._transcode_result

    @transcode_result.setter
    def transcode_result(self, transcode_result):
        r"""Sets the transcode_result of this Result.

        :param transcode_result: The transcode_result of this Result.
        :type transcode_result: :class:`huaweicloudsdkvod.v1.TranscodeInfoResult`
        """
        self._transcode_result = transcode_result

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
        if not isinstance(other, Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
