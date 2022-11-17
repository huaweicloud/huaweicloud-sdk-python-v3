# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestPlanJournalDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'updated': 'list[AttributeChange]',
        'added': 'list[NameAndId]',
        'deleted': 'list[NameAndId]',
        'journalized_type': 'str',
        'type': 'str'
    }

    attribute_map = {
        'updated': 'updated',
        'added': 'added',
        'deleted': 'deleted',
        'journalized_type': 'journalized_type',
        'type': 'type'
    }

    def __init__(self, updated=None, added=None, deleted=None, journalized_type=None, type=None):
        """TestPlanJournalDetail

        The model defined in huaweicloud sdk

        :param updated: 测试计划基础信息变更，包括计划名称，测试类型，计划处理者、版本号、关联迭代、开始日期、截至日期、描述
        :type updated: list[:class:`huaweicloudsdkcloudtest.v1.AttributeChange`]
        :param added: 测试计划资源的添加记录（工作项或者测试用例）
        :type added: list[:class:`huaweicloudsdkcloudtest.v1.NameAndId`]
        :param deleted: 测试计划资源的移除记录（工作项或者测试用例）
        :type deleted: list[:class:`huaweicloudsdkcloudtest.v1.NameAndId`]
        :param journalized_type: 表明该条变更记录的具体变更类型，例如测试用例（testCase），需求（issue）
        :type journalized_type: str
        :param type: 表明该条变更记录属于基础信息变更还是资源（需求添加移除、用例添加移除）变更
        :type type: str
        """
        
        

        self._updated = None
        self._added = None
        self._deleted = None
        self._journalized_type = None
        self._type = None
        self.discriminator = None

        if updated is not None:
            self.updated = updated
        if added is not None:
            self.added = added
        if deleted is not None:
            self.deleted = deleted
        if journalized_type is not None:
            self.journalized_type = journalized_type
        if type is not None:
            self.type = type

    @property
    def updated(self):
        """Gets the updated of this TestPlanJournalDetail.

        测试计划基础信息变更，包括计划名称，测试类型，计划处理者、版本号、关联迭代、开始日期、截至日期、描述

        :return: The updated of this TestPlanJournalDetail.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AttributeChange`]
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this TestPlanJournalDetail.

        测试计划基础信息变更，包括计划名称，测试类型，计划处理者、版本号、关联迭代、开始日期、截至日期、描述

        :param updated: The updated of this TestPlanJournalDetail.
        :type updated: list[:class:`huaweicloudsdkcloudtest.v1.AttributeChange`]
        """
        self._updated = updated

    @property
    def added(self):
        """Gets the added of this TestPlanJournalDetail.

        测试计划资源的添加记录（工作项或者测试用例）

        :return: The added of this TestPlanJournalDetail.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.NameAndId`]
        """
        return self._added

    @added.setter
    def added(self, added):
        """Sets the added of this TestPlanJournalDetail.

        测试计划资源的添加记录（工作项或者测试用例）

        :param added: The added of this TestPlanJournalDetail.
        :type added: list[:class:`huaweicloudsdkcloudtest.v1.NameAndId`]
        """
        self._added = added

    @property
    def deleted(self):
        """Gets the deleted of this TestPlanJournalDetail.

        测试计划资源的移除记录（工作项或者测试用例）

        :return: The deleted of this TestPlanJournalDetail.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.NameAndId`]
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this TestPlanJournalDetail.

        测试计划资源的移除记录（工作项或者测试用例）

        :param deleted: The deleted of this TestPlanJournalDetail.
        :type deleted: list[:class:`huaweicloudsdkcloudtest.v1.NameAndId`]
        """
        self._deleted = deleted

    @property
    def journalized_type(self):
        """Gets the journalized_type of this TestPlanJournalDetail.

        表明该条变更记录的具体变更类型，例如测试用例（testCase），需求（issue）

        :return: The journalized_type of this TestPlanJournalDetail.
        :rtype: str
        """
        return self._journalized_type

    @journalized_type.setter
    def journalized_type(self, journalized_type):
        """Sets the journalized_type of this TestPlanJournalDetail.

        表明该条变更记录的具体变更类型，例如测试用例（testCase），需求（issue）

        :param journalized_type: The journalized_type of this TestPlanJournalDetail.
        :type journalized_type: str
        """
        self._journalized_type = journalized_type

    @property
    def type(self):
        """Gets the type of this TestPlanJournalDetail.

        表明该条变更记录属于基础信息变更还是资源（需求添加移除、用例添加移除）变更

        :return: The type of this TestPlanJournalDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TestPlanJournalDetail.

        表明该条变更记录属于基础信息变更还是资源（需求添加移除、用例添加移除）变更

        :param type: The type of this TestPlanJournalDetail.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, TestPlanJournalDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
