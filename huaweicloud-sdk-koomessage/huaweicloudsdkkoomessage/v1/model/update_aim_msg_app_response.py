# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAimMsgAppResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'app_id': 'str'
    }

    attribute_map = {
        'app_name': 'app_name',
        'app_id': 'app_id'
    }

    def __init__(self, app_name=None, app_id=None):
        r"""UpdateAimMsgAppResponse

        The model defined in huaweicloud sdk

        :param app_name: 应用名称。
        :type app_name: str
        :param app_id: 应用ID。
        :type app_id: str
        """
        
        super(UpdateAimMsgAppResponse, self).__init__()

        self._app_name = None
        self._app_id = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        if app_id is not None:
            self.app_id = app_id

    @property
    def app_name(self):
        r"""Gets the app_name of this UpdateAimMsgAppResponse.

        应用名称。

        :return: The app_name of this UpdateAimMsgAppResponse.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this UpdateAimMsgAppResponse.

        应用名称。

        :param app_name: The app_name of this UpdateAimMsgAppResponse.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_id(self):
        r"""Gets the app_id of this UpdateAimMsgAppResponse.

        应用ID。

        :return: The app_id of this UpdateAimMsgAppResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this UpdateAimMsgAppResponse.

        应用ID。

        :param app_id: The app_id of this UpdateAimMsgAppResponse.
        :type app_id: str
        """
        self._app_id = app_id

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
        if not isinstance(other, UpdateAimMsgAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
