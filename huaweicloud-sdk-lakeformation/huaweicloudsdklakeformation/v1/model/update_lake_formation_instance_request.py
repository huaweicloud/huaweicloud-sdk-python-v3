# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLakeFormationInstanceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'body': 'UpdateLakeFormationInstance'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'body': 'body'
    }

    def __init__(self, instance_id=None, body=None):
        """UpdateLakeFormationInstanceRequest

        The model defined in huaweicloud sdk

        :param instance_id: LakeFormation实例ID
        :type instance_id: str
        :param body: Body of the UpdateLakeFormationInstanceRequest
        :type body: :class:`huaweicloudsdklakeformation.v1.UpdateLakeFormationInstance`
        """
        
        

        self._instance_id = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        """Gets the instance_id of this UpdateLakeFormationInstanceRequest.

        LakeFormation实例ID

        :return: The instance_id of this UpdateLakeFormationInstanceRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this UpdateLakeFormationInstanceRequest.

        LakeFormation实例ID

        :param instance_id: The instance_id of this UpdateLakeFormationInstanceRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def body(self):
        """Gets the body of this UpdateLakeFormationInstanceRequest.

        :return: The body of this UpdateLakeFormationInstanceRequest.
        :rtype: :class:`huaweicloudsdklakeformation.v1.UpdateLakeFormationInstance`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateLakeFormationInstanceRequest.

        :param body: The body of this UpdateLakeFormationInstanceRequest.
        :type body: :class:`huaweicloudsdklakeformation.v1.UpdateLakeFormationInstance`
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
        if not isinstance(other, UpdateLakeFormationInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
