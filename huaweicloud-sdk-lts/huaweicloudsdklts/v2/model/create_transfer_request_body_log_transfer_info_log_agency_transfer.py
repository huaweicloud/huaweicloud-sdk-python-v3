# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'agency_domain_id': 'str',
        'agency_domain_name': 'str',
        'agency_name': 'str',
        'agency_project_id': 'str',
        'be_agency_domain_id': 'str',
        'be_agency_project_id': 'str'
    }

    attribute_map = {
        'agency_domain_id': 'agency_domain_id',
        'agency_domain_name': 'agency_domain_name',
        'agency_name': 'agency_name',
        'agency_project_id': 'agency_project_id',
        'be_agency_domain_id': 'be_agency_domain_id',
        'be_agency_project_id': 'be_agency_project_id'
    }

    def __init__(self, agency_domain_id=None, agency_domain_name=None, agency_name=None, agency_project_id=None, be_agency_domain_id=None, be_agency_project_id=None):
        """CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer

        The model defined in huaweicloud sdk

        :param agency_domain_id: 委托方账号ID
        :type agency_domain_id: str
        :param agency_domain_name: 委托方账号名称
        :type agency_domain_name: str
        :param agency_name: 委托方配置的委托名称
        :type agency_name: str
        :param agency_project_id: 委托方项目ID
        :type agency_project_id: str
        :param be_agency_domain_id: 被委托方账号ID，实际配置转储的账号ID
        :type be_agency_domain_id: str
        :param be_agency_project_id: 被委托方项目ID，实际配置转储的账号的项目ID
        :type be_agency_project_id: str
        """
        
        

        self._agency_domain_id = None
        self._agency_domain_name = None
        self._agency_name = None
        self._agency_project_id = None
        self._be_agency_domain_id = None
        self._be_agency_project_id = None
        self.discriminator = None

        self.agency_domain_id = agency_domain_id
        self.agency_domain_name = agency_domain_name
        self.agency_name = agency_name
        self.agency_project_id = agency_project_id
        self.be_agency_domain_id = be_agency_domain_id
        self.be_agency_project_id = be_agency_project_id

    @property
    def agency_domain_id(self):
        """Gets the agency_domain_id of this CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer.

        委托方账号ID

        :return: The agency_domain_id of this CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer.
        :rtype: str
        """
        return self._agency_domain_id

    @agency_domain_id.setter
    def agency_domain_id(self, agency_domain_id):
        """Sets the agency_domain_id of this CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer.

        委托方账号ID

        :param agency_domain_id: The agency_domain_id of this CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer.
        :type agency_domain_id: str
        """
        self._agency_domain_id = agency_domain_id

    @property
    def agency_domain_name(self):
        """Gets the agency_domain_name of this CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer.

        委托方账号名称

        :return: The agency_domain_name of this CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer.
        :rtype: str
        """
        return self._agency_domain_name

    @agency_domain_name.setter
    def agency_domain_name(self, agency_domain_name):
        """Sets the agency_domain_name of this CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer.

        委托方账号名称

        :param agency_domain_name: The agency_domain_name of this CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer.
        :type agency_domain_name: str
        """
        self._agency_domain_name = agency_domain_name

    @property
    def agency_name(self):
        """Gets the agency_name of this CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer.

        委托方配置的委托名称

        :return: The agency_name of this CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        """Sets the agency_name of this CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer.

        委托方配置的委托名称

        :param agency_name: The agency_name of this CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def agency_project_id(self):
        """Gets the agency_project_id of this CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer.

        委托方项目ID

        :return: The agency_project_id of this CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer.
        :rtype: str
        """
        return self._agency_project_id

    @agency_project_id.setter
    def agency_project_id(self, agency_project_id):
        """Sets the agency_project_id of this CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer.

        委托方项目ID

        :param agency_project_id: The agency_project_id of this CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer.
        :type agency_project_id: str
        """
        self._agency_project_id = agency_project_id

    @property
    def be_agency_domain_id(self):
        """Gets the be_agency_domain_id of this CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer.

        被委托方账号ID，实际配置转储的账号ID

        :return: The be_agency_domain_id of this CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer.
        :rtype: str
        """
        return self._be_agency_domain_id

    @be_agency_domain_id.setter
    def be_agency_domain_id(self, be_agency_domain_id):
        """Sets the be_agency_domain_id of this CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer.

        被委托方账号ID，实际配置转储的账号ID

        :param be_agency_domain_id: The be_agency_domain_id of this CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer.
        :type be_agency_domain_id: str
        """
        self._be_agency_domain_id = be_agency_domain_id

    @property
    def be_agency_project_id(self):
        """Gets the be_agency_project_id of this CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer.

        被委托方项目ID，实际配置转储的账号的项目ID

        :return: The be_agency_project_id of this CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer.
        :rtype: str
        """
        return self._be_agency_project_id

    @be_agency_project_id.setter
    def be_agency_project_id(self, be_agency_project_id):
        """Sets the be_agency_project_id of this CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer.

        被委托方项目ID，实际配置转储的账号的项目ID

        :param be_agency_project_id: The be_agency_project_id of this CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer.
        :type be_agency_project_id: str
        """
        self._be_agency_project_id = be_agency_project_id

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
        if not isinstance(other, CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
