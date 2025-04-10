# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkItemInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'work_item_id': 'str',
        'has_child': 'bool',
        'is_open': 'bool',
        'child_list': 'list[WorkItemInfo]'
    }

    attribute_map = {
        'work_item_id': 'work_item_id',
        'has_child': 'has_child',
        'is_open': 'is_open',
        'child_list': 'child_list'
    }

    def __init__(self, work_item_id=None, has_child=None, is_open=None, child_list=None):
        r"""WorkItemInfo

        The model defined in huaweicloud sdk

        :param work_item_id: 工作项编号
        :type work_item_id: str
        :param has_child: 是否有子需求
        :type has_child: bool
        :param is_open: 是否展开
        :type is_open: bool
        :param child_list: 子需求
        :type child_list: list[:class:`huaweicloudsdkcloudtest.v1.WorkItemInfo`]
        """
        
        

        self._work_item_id = None
        self._has_child = None
        self._is_open = None
        self._child_list = None
        self.discriminator = None

        self.work_item_id = work_item_id
        self.has_child = has_child
        self.is_open = is_open
        if child_list is not None:
            self.child_list = child_list

    @property
    def work_item_id(self):
        r"""Gets the work_item_id of this WorkItemInfo.

        工作项编号

        :return: The work_item_id of this WorkItemInfo.
        :rtype: str
        """
        return self._work_item_id

    @work_item_id.setter
    def work_item_id(self, work_item_id):
        r"""Sets the work_item_id of this WorkItemInfo.

        工作项编号

        :param work_item_id: The work_item_id of this WorkItemInfo.
        :type work_item_id: str
        """
        self._work_item_id = work_item_id

    @property
    def has_child(self):
        r"""Gets the has_child of this WorkItemInfo.

        是否有子需求

        :return: The has_child of this WorkItemInfo.
        :rtype: bool
        """
        return self._has_child

    @has_child.setter
    def has_child(self, has_child):
        r"""Sets the has_child of this WorkItemInfo.

        是否有子需求

        :param has_child: The has_child of this WorkItemInfo.
        :type has_child: bool
        """
        self._has_child = has_child

    @property
    def is_open(self):
        r"""Gets the is_open of this WorkItemInfo.

        是否展开

        :return: The is_open of this WorkItemInfo.
        :rtype: bool
        """
        return self._is_open

    @is_open.setter
    def is_open(self, is_open):
        r"""Sets the is_open of this WorkItemInfo.

        是否展开

        :param is_open: The is_open of this WorkItemInfo.
        :type is_open: bool
        """
        self._is_open = is_open

    @property
    def child_list(self):
        r"""Gets the child_list of this WorkItemInfo.

        子需求

        :return: The child_list of this WorkItemInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.WorkItemInfo`]
        """
        return self._child_list

    @child_list.setter
    def child_list(self, child_list):
        r"""Sets the child_list of this WorkItemInfo.

        子需求

        :param child_list: The child_list of this WorkItemInfo.
        :type child_list: list[:class:`huaweicloudsdkcloudtest.v1.WorkItemInfo`]
        """
        self._child_list = child_list

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
        if not isinstance(other, WorkItemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
