# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateObjectRetrievalRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'obs_info': 'ObsInfo',
        'days': 'int',
        'callback_url': 'str',
        'session_context': 'str'
    }

    attribute_map = {
        'obs_info': 'obs_info',
        'days': 'days',
        'callback_url': 'callback_url',
        'session_context': 'session_context'
    }

    def __init__(self, obs_info=None, days=None, callback_url=None, session_context=None):
        r"""CreateObjectRetrievalRequestBody

        The model defined in huaweicloud sdk

        :param obs_info: 
        :type obs_info: :class:`huaweicloudsdkvod.v1.ObsInfo`
        :param days: 临时恢复时间，临时恢复会产生一个标准存储副本，副本的存在时间。单位：天，默认1天。 
        :type days: int
        :param callback_url: 回调地址，为空则不回调
        :type callback_url: str
        :param session_context: 自定义上下文，回调时会回调给用户，透传信息
        :type session_context: str
        """
        
        

        self._obs_info = None
        self._days = None
        self._callback_url = None
        self._session_context = None
        self.discriminator = None

        self.obs_info = obs_info
        if days is not None:
            self.days = days
        if callback_url is not None:
            self.callback_url = callback_url
        if session_context is not None:
            self.session_context = session_context

    @property
    def obs_info(self):
        r"""Gets the obs_info of this CreateObjectRetrievalRequestBody.

        :return: The obs_info of this CreateObjectRetrievalRequestBody.
        :rtype: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        return self._obs_info

    @obs_info.setter
    def obs_info(self, obs_info):
        r"""Sets the obs_info of this CreateObjectRetrievalRequestBody.

        :param obs_info: The obs_info of this CreateObjectRetrievalRequestBody.
        :type obs_info: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        self._obs_info = obs_info

    @property
    def days(self):
        r"""Gets the days of this CreateObjectRetrievalRequestBody.

        临时恢复时间，临时恢复会产生一个标准存储副本，副本的存在时间。单位：天，默认1天。 

        :return: The days of this CreateObjectRetrievalRequestBody.
        :rtype: int
        """
        return self._days

    @days.setter
    def days(self, days):
        r"""Sets the days of this CreateObjectRetrievalRequestBody.

        临时恢复时间，临时恢复会产生一个标准存储副本，副本的存在时间。单位：天，默认1天。 

        :param days: The days of this CreateObjectRetrievalRequestBody.
        :type days: int
        """
        self._days = days

    @property
    def callback_url(self):
        r"""Gets the callback_url of this CreateObjectRetrievalRequestBody.

        回调地址，为空则不回调

        :return: The callback_url of this CreateObjectRetrievalRequestBody.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        r"""Sets the callback_url of this CreateObjectRetrievalRequestBody.

        回调地址，为空则不回调

        :param callback_url: The callback_url of this CreateObjectRetrievalRequestBody.
        :type callback_url: str
        """
        self._callback_url = callback_url

    @property
    def session_context(self):
        r"""Gets the session_context of this CreateObjectRetrievalRequestBody.

        自定义上下文，回调时会回调给用户，透传信息

        :return: The session_context of this CreateObjectRetrievalRequestBody.
        :rtype: str
        """
        return self._session_context

    @session_context.setter
    def session_context(self, session_context):
        r"""Sets the session_context of this CreateObjectRetrievalRequestBody.

        自定义上下文，回调时会回调给用户，透传信息

        :param session_context: The session_context of this CreateObjectRetrievalRequestBody.
        :type session_context: str
        """
        self._session_context = session_context

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
        if not isinstance(other, CreateObjectRetrievalRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
