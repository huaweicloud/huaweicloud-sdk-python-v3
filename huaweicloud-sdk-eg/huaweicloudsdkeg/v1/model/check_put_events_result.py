# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckPutEventsResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'channel_id': 'str',
        'source_name': 'str',
        'check_result': 'bool',
        'check_detail': 'str'
    }

    attribute_map = {
        'channel_id': 'channel_id',
        'source_name': 'source_name',
        'check_result': 'check_result',
        'check_detail': 'check_detail'
    }

    def __init__(self, channel_id=None, source_name=None, check_result=None, check_detail=None):
        """CheckPutEventsResult

        The model defined in huaweicloud sdk

        :param channel_id: 事件通道id
        :type channel_id: str
        :param source_name: 事件源名称
        :type source_name: str
        :param check_result: 发送事件是否成功检查结果
        :type check_result: bool
        :param check_detail: 发送事件是否成功检查明细
        :type check_detail: str
        """
        
        

        self._channel_id = None
        self._source_name = None
        self._check_result = None
        self._check_detail = None
        self.discriminator = None

        if channel_id is not None:
            self.channel_id = channel_id
        if source_name is not None:
            self.source_name = source_name
        if check_result is not None:
            self.check_result = check_result
        if check_detail is not None:
            self.check_detail = check_detail

    @property
    def channel_id(self):
        """Gets the channel_id of this CheckPutEventsResult.

        事件通道id

        :return: The channel_id of this CheckPutEventsResult.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this CheckPutEventsResult.

        事件通道id

        :param channel_id: The channel_id of this CheckPutEventsResult.
        :type channel_id: str
        """
        self._channel_id = channel_id

    @property
    def source_name(self):
        """Gets the source_name of this CheckPutEventsResult.

        事件源名称

        :return: The source_name of this CheckPutEventsResult.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """Sets the source_name of this CheckPutEventsResult.

        事件源名称

        :param source_name: The source_name of this CheckPutEventsResult.
        :type source_name: str
        """
        self._source_name = source_name

    @property
    def check_result(self):
        """Gets the check_result of this CheckPutEventsResult.

        发送事件是否成功检查结果

        :return: The check_result of this CheckPutEventsResult.
        :rtype: bool
        """
        return self._check_result

    @check_result.setter
    def check_result(self, check_result):
        """Sets the check_result of this CheckPutEventsResult.

        发送事件是否成功检查结果

        :param check_result: The check_result of this CheckPutEventsResult.
        :type check_result: bool
        """
        self._check_result = check_result

    @property
    def check_detail(self):
        """Gets the check_detail of this CheckPutEventsResult.

        发送事件是否成功检查明细

        :return: The check_detail of this CheckPutEventsResult.
        :rtype: str
        """
        return self._check_detail

    @check_detail.setter
    def check_detail(self, check_detail):
        """Sets the check_detail of this CheckPutEventsResult.

        发送事件是否成功检查明细

        :param check_detail: The check_detail of this CheckPutEventsResult.
        :type check_detail: str
        """
        self._check_detail = check_detail

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
        if not isinstance(other, CheckPutEventsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
