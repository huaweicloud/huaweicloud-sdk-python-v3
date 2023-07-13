# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssignShareFolderReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'storage_claim_id': 'str',
        'add_items': 'list[Assignment]',
        'del_items': 'list[Attachment]'
    }

    attribute_map = {
        'storage_claim_id': 'storage_claim_id',
        'add_items': 'add_items',
        'del_items': 'del_items'
    }

    def __init__(self, storage_claim_id=None, add_items=None, del_items=None):
        """AssignShareFolderReq

        The model defined in huaweicloud sdk

        :param storage_claim_id: WKS存储目录声明ID
        :type storage_claim_id: str
        :param add_items: 增加的成员列表
        :type add_items: list[:class:`huaweicloudsdkworkspaceapp.v1.Assignment`]
        :param del_items: 移除的成员列表
        :type del_items: list[:class:`huaweicloudsdkworkspaceapp.v1.Attachment`]
        """
        
        

        self._storage_claim_id = None
        self._add_items = None
        self._del_items = None
        self.discriminator = None

        self.storage_claim_id = storage_claim_id
        if add_items is not None:
            self.add_items = add_items
        if del_items is not None:
            self.del_items = del_items

    @property
    def storage_claim_id(self):
        """Gets the storage_claim_id of this AssignShareFolderReq.

        WKS存储目录声明ID

        :return: The storage_claim_id of this AssignShareFolderReq.
        :rtype: str
        """
        return self._storage_claim_id

    @storage_claim_id.setter
    def storage_claim_id(self, storage_claim_id):
        """Sets the storage_claim_id of this AssignShareFolderReq.

        WKS存储目录声明ID

        :param storage_claim_id: The storage_claim_id of this AssignShareFolderReq.
        :type storage_claim_id: str
        """
        self._storage_claim_id = storage_claim_id

    @property
    def add_items(self):
        """Gets the add_items of this AssignShareFolderReq.

        增加的成员列表

        :return: The add_items of this AssignShareFolderReq.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.Assignment`]
        """
        return self._add_items

    @add_items.setter
    def add_items(self, add_items):
        """Sets the add_items of this AssignShareFolderReq.

        增加的成员列表

        :param add_items: The add_items of this AssignShareFolderReq.
        :type add_items: list[:class:`huaweicloudsdkworkspaceapp.v1.Assignment`]
        """
        self._add_items = add_items

    @property
    def del_items(self):
        """Gets the del_items of this AssignShareFolderReq.

        移除的成员列表

        :return: The del_items of this AssignShareFolderReq.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.Attachment`]
        """
        return self._del_items

    @del_items.setter
    def del_items(self, del_items):
        """Sets the del_items of this AssignShareFolderReq.

        移除的成员列表

        :param del_items: The del_items of this AssignShareFolderReq.
        :type del_items: list[:class:`huaweicloudsdkworkspaceapp.v1.Attachment`]
        """
        self._del_items = del_items

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
        if not isinstance(other, AssignShareFolderReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
