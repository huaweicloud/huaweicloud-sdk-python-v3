# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddRdsNoAgentDatabaseResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'illegal_db_id': 'list[str]',
        'legal_db_id': 'list[str]'
    }

    attribute_map = {
        'illegal_db_id': 'illegal_db_id',
        'legal_db_id': 'legal_db_id'
    }

    def __init__(self, illegal_db_id=None, legal_db_id=None):
        """AddRdsNoAgentDatabaseResponse

        The model defined in huaweicloud sdk

        :param illegal_db_id: 添加失败的数据库实例id
        :type illegal_db_id: list[str]
        :param legal_db_id: 添加成功的数据库实例id
        :type legal_db_id: list[str]
        """
        
        super(AddRdsNoAgentDatabaseResponse, self).__init__()

        self._illegal_db_id = None
        self._legal_db_id = None
        self.discriminator = None

        if illegal_db_id is not None:
            self.illegal_db_id = illegal_db_id
        if legal_db_id is not None:
            self.legal_db_id = legal_db_id

    @property
    def illegal_db_id(self):
        """Gets the illegal_db_id of this AddRdsNoAgentDatabaseResponse.

        添加失败的数据库实例id

        :return: The illegal_db_id of this AddRdsNoAgentDatabaseResponse.
        :rtype: list[str]
        """
        return self._illegal_db_id

    @illegal_db_id.setter
    def illegal_db_id(self, illegal_db_id):
        """Sets the illegal_db_id of this AddRdsNoAgentDatabaseResponse.

        添加失败的数据库实例id

        :param illegal_db_id: The illegal_db_id of this AddRdsNoAgentDatabaseResponse.
        :type illegal_db_id: list[str]
        """
        self._illegal_db_id = illegal_db_id

    @property
    def legal_db_id(self):
        """Gets the legal_db_id of this AddRdsNoAgentDatabaseResponse.

        添加成功的数据库实例id

        :return: The legal_db_id of this AddRdsNoAgentDatabaseResponse.
        :rtype: list[str]
        """
        return self._legal_db_id

    @legal_db_id.setter
    def legal_db_id(self, legal_db_id):
        """Sets the legal_db_id of this AddRdsNoAgentDatabaseResponse.

        添加成功的数据库实例id

        :param legal_db_id: The legal_db_id of this AddRdsNoAgentDatabaseResponse.
        :type legal_db_id: list[str]
        """
        self._legal_db_id = legal_db_id

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
        if not isinstance(other, AddRdsNoAgentDatabaseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
