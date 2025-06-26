# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateIntranetAccessRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'description': 'description'
    }

    def __init__(self, project_id=None, vpc_id=None, subnet_id=None, description=None):
        r"""CreateIntranetAccessRequestBody

        The model defined in huaweicloud sdk

        :param project_id: vpc和子网所在项目的编号
        :type project_id: str
        :param vpc_id: vpc编号ID
        :type vpc_id: str
        :param subnet_id: 子网编号ID
        :type subnet_id: str
        :param description: 描述
        :type description: str
        """
        
        

        self._project_id = None
        self._vpc_id = None
        self._subnet_id = None
        self._description = None
        self.discriminator = None

        self.project_id = project_id
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        if description is not None:
            self.description = description

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateIntranetAccessRequestBody.

        vpc和子网所在项目的编号

        :return: The project_id of this CreateIntranetAccessRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateIntranetAccessRequestBody.

        vpc和子网所在项目的编号

        :param project_id: The project_id of this CreateIntranetAccessRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateIntranetAccessRequestBody.

        vpc编号ID

        :return: The vpc_id of this CreateIntranetAccessRequestBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateIntranetAccessRequestBody.

        vpc编号ID

        :param vpc_id: The vpc_id of this CreateIntranetAccessRequestBody.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CreateIntranetAccessRequestBody.

        子网编号ID

        :return: The subnet_id of this CreateIntranetAccessRequestBody.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CreateIntranetAccessRequestBody.

        子网编号ID

        :param subnet_id: The subnet_id of this CreateIntranetAccessRequestBody.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def description(self):
        r"""Gets the description of this CreateIntranetAccessRequestBody.

        描述

        :return: The description of this CreateIntranetAccessRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateIntranetAccessRequestBody.

        描述

        :param description: The description of this CreateIntranetAccessRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateIntranetAccessRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
