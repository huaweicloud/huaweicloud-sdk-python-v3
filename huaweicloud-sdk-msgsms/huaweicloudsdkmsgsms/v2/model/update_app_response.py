# coding: utf-8

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
        'app_key': 'str',
        'app_name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'app_key': 'app_key',
        'app_name': 'app_name',
        'id': 'id'
    }

    def __init__(self, app_key=None, app_name=None, id=None):
        r"""UpdateAppResponse

        The model defined in huaweicloud sdk

        :param app_key: 应用KEY
        :type app_key: str
        :param app_name: 应用名称
        :type app_name: str
        :param id: 应用主键ID
        :type id: str
        """
        
        super(UpdateAppResponse, self).__init__()

        self._app_key = None
        self._app_name = None
        self._id = None
        self.discriminator = None

        if app_key is not None:
            self.app_key = app_key
        if app_name is not None:
            self.app_name = app_name
        if id is not None:
            self.id = id

    @property
    def app_key(self):
        r"""Gets the app_key of this UpdateAppResponse.

        应用KEY

        :return: The app_key of this UpdateAppResponse.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        r"""Sets the app_key of this UpdateAppResponse.

        应用KEY

        :param app_key: The app_key of this UpdateAppResponse.
        :type app_key: str
        """
        self._app_key = app_key

    @property
    def app_name(self):
        r"""Gets the app_name of this UpdateAppResponse.

        应用名称

        :return: The app_name of this UpdateAppResponse.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this UpdateAppResponse.

        应用名称

        :param app_name: The app_name of this UpdateAppResponse.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def id(self):
        r"""Gets the id of this UpdateAppResponse.

        应用主键ID

        :return: The id of this UpdateAppResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateAppResponse.

        应用主键ID

        :param id: The id of this UpdateAppResponse.
        :type id: str
        """
        self._id = id

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
