# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnterpriseOrganizationsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'recursive_query': 'int',
        'parent_id': 'str'
    }

    attribute_map = {
        'recursive_query': 'recursive_query',
        'parent_id': 'parent_id'
    }

    def __init__(self, recursive_query=None, parent_id=None):
        """ListEnterpriseOrganizationsRequest

        The model defined in huaweicloud sdk

        :param recursive_query: 是否递归查询。0：不递归（默认）1：递归如果不递归，只返回起始节点的直接子节点。此参数不携带或携带值为空时，不作为筛选条件。
        :type recursive_query: int
        :param parent_id: 指定的节点ID。为空则从根节点查起。此参数不携带或携带值为空时，不作为筛选条件。 说明： 此参数须由纯数字组成。
        :type parent_id: str
        """
        
        

        self._recursive_query = None
        self._parent_id = None
        self.discriminator = None

        if recursive_query is not None:
            self.recursive_query = recursive_query
        if parent_id is not None:
            self.parent_id = parent_id

    @property
    def recursive_query(self):
        """Gets the recursive_query of this ListEnterpriseOrganizationsRequest.

        是否递归查询。0：不递归（默认）1：递归如果不递归，只返回起始节点的直接子节点。此参数不携带或携带值为空时，不作为筛选条件。

        :return: The recursive_query of this ListEnterpriseOrganizationsRequest.
        :rtype: int
        """
        return self._recursive_query

    @recursive_query.setter
    def recursive_query(self, recursive_query):
        """Sets the recursive_query of this ListEnterpriseOrganizationsRequest.

        是否递归查询。0：不递归（默认）1：递归如果不递归，只返回起始节点的直接子节点。此参数不携带或携带值为空时，不作为筛选条件。

        :param recursive_query: The recursive_query of this ListEnterpriseOrganizationsRequest.
        :type recursive_query: int
        """
        self._recursive_query = recursive_query

    @property
    def parent_id(self):
        """Gets the parent_id of this ListEnterpriseOrganizationsRequest.

        指定的节点ID。为空则从根节点查起。此参数不携带或携带值为空时，不作为筛选条件。 说明： 此参数须由纯数字组成。

        :return: The parent_id of this ListEnterpriseOrganizationsRequest.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this ListEnterpriseOrganizationsRequest.

        指定的节点ID。为空则从根节点查起。此参数不携带或携带值为空时，不作为筛选条件。 说明： 此参数须由纯数字组成。

        :param parent_id: The parent_id of this ListEnterpriseOrganizationsRequest.
        :type parent_id: str
        """
        self._parent_id = parent_id

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
        if not isinstance(other, ListEnterpriseOrganizationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
