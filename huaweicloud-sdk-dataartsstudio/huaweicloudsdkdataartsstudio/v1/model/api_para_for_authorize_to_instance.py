# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiParaForAuthorizeToInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'str',
        'app_ids': 'list[str]'
    }

    attribute_map = {
        'time': 'time',
        'app_ids': 'app_ids'
    }

    def __init__(self, time=None, app_ids=None):
        """ApiParaForAuthorizeToInstance

        The model defined in huaweicloud sdk

        :param time: 截止时间
        :type time: str
        :param app_ids: app编号列表
        :type app_ids: list[str]
        """
        
        

        self._time = None
        self._app_ids = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if app_ids is not None:
            self.app_ids = app_ids

    @property
    def time(self):
        """Gets the time of this ApiParaForAuthorizeToInstance.

        截止时间

        :return: The time of this ApiParaForAuthorizeToInstance.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ApiParaForAuthorizeToInstance.

        截止时间

        :param time: The time of this ApiParaForAuthorizeToInstance.
        :type time: str
        """
        self._time = time

    @property
    def app_ids(self):
        """Gets the app_ids of this ApiParaForAuthorizeToInstance.

        app编号列表

        :return: The app_ids of this ApiParaForAuthorizeToInstance.
        :rtype: list[str]
        """
        return self._app_ids

    @app_ids.setter
    def app_ids(self, app_ids):
        """Sets the app_ids of this ApiParaForAuthorizeToInstance.

        app编号列表

        :param app_ids: The app_ids of this ApiParaForAuthorizeToInstance.
        :type app_ids: list[str]
        """
        self._app_ids = app_ids

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
        if not isinstance(other, ApiParaForAuthorizeToInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
