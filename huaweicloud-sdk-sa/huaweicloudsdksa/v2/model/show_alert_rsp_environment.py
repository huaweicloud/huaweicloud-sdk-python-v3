# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAlertRspEnvironment:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vendor_type': 'str',
        'domain_id': 'str',
        'region_id': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'vendor_type': 'vendor_type',
        'domain_id': 'domain_id',
        'region_id': 'region_id',
        'project_id': 'project_id'
    }

    def __init__(self, vendor_type=None, domain_id=None, region_id=None, project_id=None):
        """ShowAlertRspEnvironment

        The model defined in huaweicloud sdk

        :param vendor_type: The name, display only
        :type vendor_type: str
        :param domain_id: Id value
        :type domain_id: str
        :param region_id: Id value
        :type region_id: str
        :param project_id: Id value
        :type project_id: str
        """
        
        

        self._vendor_type = None
        self._domain_id = None
        self._region_id = None
        self._project_id = None
        self.discriminator = None

        if vendor_type is not None:
            self.vendor_type = vendor_type
        if domain_id is not None:
            self.domain_id = domain_id
        if region_id is not None:
            self.region_id = region_id
        if project_id is not None:
            self.project_id = project_id

    @property
    def vendor_type(self):
        """Gets the vendor_type of this ShowAlertRspEnvironment.

        The name, display only

        :return: The vendor_type of this ShowAlertRspEnvironment.
        :rtype: str
        """
        return self._vendor_type

    @vendor_type.setter
    def vendor_type(self, vendor_type):
        """Sets the vendor_type of this ShowAlertRspEnvironment.

        The name, display only

        :param vendor_type: The vendor_type of this ShowAlertRspEnvironment.
        :type vendor_type: str
        """
        self._vendor_type = vendor_type

    @property
    def domain_id(self):
        """Gets the domain_id of this ShowAlertRspEnvironment.

        Id value

        :return: The domain_id of this ShowAlertRspEnvironment.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ShowAlertRspEnvironment.

        Id value

        :param domain_id: The domain_id of this ShowAlertRspEnvironment.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def region_id(self):
        """Gets the region_id of this ShowAlertRspEnvironment.

        Id value

        :return: The region_id of this ShowAlertRspEnvironment.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ShowAlertRspEnvironment.

        Id value

        :param region_id: The region_id of this ShowAlertRspEnvironment.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def project_id(self):
        """Gets the project_id of this ShowAlertRspEnvironment.

        Id value

        :return: The project_id of this ShowAlertRspEnvironment.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowAlertRspEnvironment.

        Id value

        :param project_id: The project_id of this ShowAlertRspEnvironment.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, ShowAlertRspEnvironment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
