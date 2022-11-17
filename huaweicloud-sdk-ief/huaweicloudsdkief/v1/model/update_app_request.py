# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAppRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ief_instance_id': 'str',
        'app_id': 'str',
        'body': 'UpdateAppBody'
    }

    attribute_map = {
        'ief_instance_id': 'ief-instance-id',
        'app_id': 'app_id',
        'body': 'body'
    }

    def __init__(self, ief_instance_id=None, app_id=None, body=None):
        """UpdateAppRequest

        The model defined in huaweicloud sdk

        :param ief_instance_id: 铂金版实例ID，专业版实例为空值
        :type ief_instance_id: str
        :param app_id: 应用模板ID
        :type app_id: str
        :param body: Body of the UpdateAppRequest
        :type body: :class:`huaweicloudsdkief.v1.UpdateAppBody`
        """
        
        

        self._ief_instance_id = None
        self._app_id = None
        self._body = None
        self.discriminator = None

        if ief_instance_id is not None:
            self.ief_instance_id = ief_instance_id
        self.app_id = app_id
        if body is not None:
            self.body = body

    @property
    def ief_instance_id(self):
        """Gets the ief_instance_id of this UpdateAppRequest.

        铂金版实例ID，专业版实例为空值

        :return: The ief_instance_id of this UpdateAppRequest.
        :rtype: str
        """
        return self._ief_instance_id

    @ief_instance_id.setter
    def ief_instance_id(self, ief_instance_id):
        """Sets the ief_instance_id of this UpdateAppRequest.

        铂金版实例ID，专业版实例为空值

        :param ief_instance_id: The ief_instance_id of this UpdateAppRequest.
        :type ief_instance_id: str
        """
        self._ief_instance_id = ief_instance_id

    @property
    def app_id(self):
        """Gets the app_id of this UpdateAppRequest.

        应用模板ID

        :return: The app_id of this UpdateAppRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this UpdateAppRequest.

        应用模板ID

        :param app_id: The app_id of this UpdateAppRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def body(self):
        """Gets the body of this UpdateAppRequest.

        :return: The body of this UpdateAppRequest.
        :rtype: :class:`huaweicloudsdkief.v1.UpdateAppBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateAppRequest.

        :param body: The body of this UpdateAppRequest.
        :type body: :class:`huaweicloudsdkief.v1.UpdateAppBody`
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
        if not isinstance(other, UpdateAppRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
