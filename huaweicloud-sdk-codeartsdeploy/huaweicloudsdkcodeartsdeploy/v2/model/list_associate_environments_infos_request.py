# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssociateEnvironmentsInfosRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'page_index': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'group_id': 'group_id',
        'page_index': 'page_index',
        'page_size': 'page_size'
    }

    def __init__(self, group_id=None, page_index=None, page_size=None):
        r"""ListAssociateEnvironmentsInfosRequest

        The model defined in huaweicloud sdk

        :param group_id: 主机集群id
        :type group_id: str
        :param page_index: 页码
        :type page_index: int
        :param page_size: 每页查询条数
        :type page_size: int
        """
        
        

        self._group_id = None
        self._page_index = None
        self._page_size = None
        self.discriminator = None

        self.group_id = group_id
        if page_index is not None:
            self.page_index = page_index
        if page_size is not None:
            self.page_size = page_size

    @property
    def group_id(self):
        r"""Gets the group_id of this ListAssociateEnvironmentsInfosRequest.

        主机集群id

        :return: The group_id of this ListAssociateEnvironmentsInfosRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListAssociateEnvironmentsInfosRequest.

        主机集群id

        :param group_id: The group_id of this ListAssociateEnvironmentsInfosRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def page_index(self):
        r"""Gets the page_index of this ListAssociateEnvironmentsInfosRequest.

        页码

        :return: The page_index of this ListAssociateEnvironmentsInfosRequest.
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        r"""Sets the page_index of this ListAssociateEnvironmentsInfosRequest.

        页码

        :param page_index: The page_index of this ListAssociateEnvironmentsInfosRequest.
        :type page_index: int
        """
        self._page_index = page_index

    @property
    def page_size(self):
        r"""Gets the page_size of this ListAssociateEnvironmentsInfosRequest.

        每页查询条数

        :return: The page_size of this ListAssociateEnvironmentsInfosRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListAssociateEnvironmentsInfosRequest.

        每页查询条数

        :param page_size: The page_size of this ListAssociateEnvironmentsInfosRequest.
        :type page_size: int
        """
        self._page_size = page_size

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
        if not isinstance(other, ListAssociateEnvironmentsInfosRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
