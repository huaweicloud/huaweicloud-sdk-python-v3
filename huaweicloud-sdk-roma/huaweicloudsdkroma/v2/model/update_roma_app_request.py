# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRomaAppRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'instance_id': 'str',
        'body': 'UpdateAppReq'
    }

    attribute_map = {
        'app_id': 'app_id',
        'instance_id': 'instance_id',
        'body': 'body'
    }

    def __init__(self, app_id=None, instance_id=None, body=None):
        r"""UpdateRomaAppRequest

        The model defined in huaweicloud sdk

        :param app_id: 应用ID
        :type app_id: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param body: Body of the UpdateRomaAppRequest
        :type body: :class:`huaweicloudsdkroma.v2.UpdateAppReq`
        """
        
        

        self._app_id = None
        self._instance_id = None
        self._body = None
        self.discriminator = None

        self.app_id = app_id
        self.instance_id = instance_id
        if body is not None:
            self.body = body

    @property
    def app_id(self):
        r"""Gets the app_id of this UpdateRomaAppRequest.

        应用ID

        :return: The app_id of this UpdateRomaAppRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this UpdateRomaAppRequest.

        应用ID

        :param app_id: The app_id of this UpdateRomaAppRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpdateRomaAppRequest.

        实例ID

        :return: The instance_id of this UpdateRomaAppRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpdateRomaAppRequest.

        实例ID

        :param instance_id: The instance_id of this UpdateRomaAppRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def body(self):
        r"""Gets the body of this UpdateRomaAppRequest.

        :return: The body of this UpdateRomaAppRequest.
        :rtype: :class:`huaweicloudsdkroma.v2.UpdateAppReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateRomaAppRequest.

        :param body: The body of this UpdateRomaAppRequest.
        :type body: :class:`huaweicloudsdkroma.v2.UpdateAppReq`
        """
        self._body = body

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
        if not isinstance(other, UpdateRomaAppRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
