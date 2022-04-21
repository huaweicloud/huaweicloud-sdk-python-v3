# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IncidentTempV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'incident_template_id': 'str',
        'incident_template_name': 'str',
        'incident_template_content': 'str'
    }

    attribute_map = {
        'incident_template_id': 'incident_template_id',
        'incident_template_name': 'incident_template_name',
        'incident_template_content': 'incident_template_content'
    }

    def __init__(self, incident_template_id=None, incident_template_name=None, incident_template_content=None):
        """IncidentTempV2

        The model defined in huaweicloud sdk

        :param incident_template_id: 模板id
        :type incident_template_id: str
        :param incident_template_name: 模板名称
        :type incident_template_name: str
        :param incident_template_content: 模板内容
        :type incident_template_content: str
        """
        
        

        self._incident_template_id = None
        self._incident_template_name = None
        self._incident_template_content = None
        self.discriminator = None

        if incident_template_id is not None:
            self.incident_template_id = incident_template_id
        if incident_template_name is not None:
            self.incident_template_name = incident_template_name
        if incident_template_content is not None:
            self.incident_template_content = incident_template_content

    @property
    def incident_template_id(self):
        """Gets the incident_template_id of this IncidentTempV2.

        模板id

        :return: The incident_template_id of this IncidentTempV2.
        :rtype: str
        """
        return self._incident_template_id

    @incident_template_id.setter
    def incident_template_id(self, incident_template_id):
        """Sets the incident_template_id of this IncidentTempV2.

        模板id

        :param incident_template_id: The incident_template_id of this IncidentTempV2.
        :type incident_template_id: str
        """
        self._incident_template_id = incident_template_id

    @property
    def incident_template_name(self):
        """Gets the incident_template_name of this IncidentTempV2.

        模板名称

        :return: The incident_template_name of this IncidentTempV2.
        :rtype: str
        """
        return self._incident_template_name

    @incident_template_name.setter
    def incident_template_name(self, incident_template_name):
        """Sets the incident_template_name of this IncidentTempV2.

        模板名称

        :param incident_template_name: The incident_template_name of this IncidentTempV2.
        :type incident_template_name: str
        """
        self._incident_template_name = incident_template_name

    @property
    def incident_template_content(self):
        """Gets the incident_template_content of this IncidentTempV2.

        模板内容

        :return: The incident_template_content of this IncidentTempV2.
        :rtype: str
        """
        return self._incident_template_content

    @incident_template_content.setter
    def incident_template_content(self, incident_template_content):
        """Sets the incident_template_content of this IncidentTempV2.

        模板内容

        :param incident_template_content: The incident_template_content of this IncidentTempV2.
        :type incident_template_content: str
        """
        self._incident_template_content = incident_template_content

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
        if not isinstance(other, IncidentTempV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
