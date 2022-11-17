# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAppResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app': 'AppResp'
    }

    attribute_map = {
        'app': 'app'
    }

    def __init__(self, app=None):
        """UpdateAppResponse

        The model defined in huaweicloud sdk

        :param app: 
        :type app: :class:`huaweicloudsdkief.v1.AppResp`
        """
        
        super(UpdateAppResponse, self).__init__()

        self._app = None
        self.discriminator = None

        if app is not None:
            self.app = app

    @property
    def app(self):
        """Gets the app of this UpdateAppResponse.

        :return: The app of this UpdateAppResponse.
        :rtype: :class:`huaweicloudsdkief.v1.AppResp`
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this UpdateAppResponse.

        :param app: The app of this UpdateAppResponse.
        :type app: :class:`huaweicloudsdkief.v1.AppResp`
        """
        self._app = app

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
        if not isinstance(other, UpdateAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
