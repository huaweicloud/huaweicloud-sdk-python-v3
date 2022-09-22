# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateMigprojectRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'mig_project_id': 'str',
        'body': 'MigProject'
    }

    attribute_map = {
        'mig_project_id': 'mig_project_id',
        'body': 'body'
    }

    def __init__(self, mig_project_id=None, body=None):
        """UpdateMigprojectRequest

        The model defined in huaweicloud sdk

        :param mig_project_id: 迁移项目ID
        :type mig_project_id: str
        :param body: Body of the UpdateMigprojectRequest
        :type body: :class:`huaweicloudsdksms.v3.MigProject`
        """
        
        

        self._mig_project_id = None
        self._body = None
        self.discriminator = None

        self.mig_project_id = mig_project_id
        if body is not None:
            self.body = body

    @property
    def mig_project_id(self):
        """Gets the mig_project_id of this UpdateMigprojectRequest.

        迁移项目ID

        :return: The mig_project_id of this UpdateMigprojectRequest.
        :rtype: str
        """
        return self._mig_project_id

    @mig_project_id.setter
    def mig_project_id(self, mig_project_id):
        """Sets the mig_project_id of this UpdateMigprojectRequest.

        迁移项目ID

        :param mig_project_id: The mig_project_id of this UpdateMigprojectRequest.
        :type mig_project_id: str
        """
        self._mig_project_id = mig_project_id

    @property
    def body(self):
        """Gets the body of this UpdateMigprojectRequest.


        :return: The body of this UpdateMigprojectRequest.
        :rtype: :class:`huaweicloudsdksms.v3.MigProject`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateMigprojectRequest.


        :param body: The body of this UpdateMigprojectRequest.
        :type body: :class:`huaweicloudsdksms.v3.MigProject`
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
        if not isinstance(other, UpdateMigprojectRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
