# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityDataClassificationRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'offset': 'int',
        'limit': 'int',
        'secrecy_level': 'str',
        'name': 'str',
        'creator': 'str',
        'enable': 'bool',
        'start_time': 'int',
        'end_time': 'int',
        'order_by': 'str',
        'desc': 'bool'
    }

    attribute_map = {
        'workspace': 'workspace',
        'offset': 'offset',
        'limit': 'limit',
        'secrecy_level': 'secrecy_level',
        'name': 'name',
        'creator': 'creator',
        'enable': 'enable',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'order_by': 'order_by',
        'desc': 'desc'
    }

    def __init__(self, workspace=None, offset=None, limit=None, secrecy_level=None, name=None, creator=None, enable=None, start_time=None, end_time=None, order_by=None, desc=None):
        r"""ListSecurityDataClassificationRulesRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param offset: 查询偏移
        :type offset: int
        :param limit: 查询一页限制
        :type limit: int
        :param secrecy_level: 密级
        :type secrecy_level: str
        :param name: 规则名称
        :type name: str
        :param creator: 规则创建者
        :type creator: str
        :param enable: 规则是否开启
        :type enable: bool
        :param start_time: 开始日期
        :type start_time: int
        :param end_time: 结束日期
        :type end_time: int
        :param order_by: 排序字段, createdAt, createdBy, updatedAt, updatedBy, name, description
        :type order_by: str
        :param desc: 排序规则
        :type desc: bool
        """
        
        

        self._workspace = None
        self._offset = None
        self._limit = None
        self._secrecy_level = None
        self._name = None
        self._creator = None
        self._enable = None
        self._start_time = None
        self._end_time = None
        self._order_by = None
        self._desc = None
        self.discriminator = None

        self.workspace = workspace
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if secrecy_level is not None:
            self.secrecy_level = secrecy_level
        if name is not None:
            self.name = name
        if creator is not None:
            self.creator = creator
        if enable is not None:
            self.enable = enable
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if order_by is not None:
            self.order_by = order_by
        if desc is not None:
            self.desc = desc

    @property
    def workspace(self):
        r"""Gets the workspace of this ListSecurityDataClassificationRulesRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListSecurityDataClassificationRulesRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListSecurityDataClassificationRulesRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListSecurityDataClassificationRulesRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def offset(self):
        r"""Gets the offset of this ListSecurityDataClassificationRulesRequest.

        查询偏移

        :return: The offset of this ListSecurityDataClassificationRulesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSecurityDataClassificationRulesRequest.

        查询偏移

        :param offset: The offset of this ListSecurityDataClassificationRulesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSecurityDataClassificationRulesRequest.

        查询一页限制

        :return: The limit of this ListSecurityDataClassificationRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSecurityDataClassificationRulesRequest.

        查询一页限制

        :param limit: The limit of this ListSecurityDataClassificationRulesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def secrecy_level(self):
        r"""Gets the secrecy_level of this ListSecurityDataClassificationRulesRequest.

        密级

        :return: The secrecy_level of this ListSecurityDataClassificationRulesRequest.
        :rtype: str
        """
        return self._secrecy_level

    @secrecy_level.setter
    def secrecy_level(self, secrecy_level):
        r"""Sets the secrecy_level of this ListSecurityDataClassificationRulesRequest.

        密级

        :param secrecy_level: The secrecy_level of this ListSecurityDataClassificationRulesRequest.
        :type secrecy_level: str
        """
        self._secrecy_level = secrecy_level

    @property
    def name(self):
        r"""Gets the name of this ListSecurityDataClassificationRulesRequest.

        规则名称

        :return: The name of this ListSecurityDataClassificationRulesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListSecurityDataClassificationRulesRequest.

        规则名称

        :param name: The name of this ListSecurityDataClassificationRulesRequest.
        :type name: str
        """
        self._name = name

    @property
    def creator(self):
        r"""Gets the creator of this ListSecurityDataClassificationRulesRequest.

        规则创建者

        :return: The creator of this ListSecurityDataClassificationRulesRequest.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ListSecurityDataClassificationRulesRequest.

        规则创建者

        :param creator: The creator of this ListSecurityDataClassificationRulesRequest.
        :type creator: str
        """
        self._creator = creator

    @property
    def enable(self):
        r"""Gets the enable of this ListSecurityDataClassificationRulesRequest.

        规则是否开启

        :return: The enable of this ListSecurityDataClassificationRulesRequest.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this ListSecurityDataClassificationRulesRequest.

        规则是否开启

        :param enable: The enable of this ListSecurityDataClassificationRulesRequest.
        :type enable: bool
        """
        self._enable = enable

    @property
    def start_time(self):
        r"""Gets the start_time of this ListSecurityDataClassificationRulesRequest.

        开始日期

        :return: The start_time of this ListSecurityDataClassificationRulesRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListSecurityDataClassificationRulesRequest.

        开始日期

        :param start_time: The start_time of this ListSecurityDataClassificationRulesRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListSecurityDataClassificationRulesRequest.

        结束日期

        :return: The end_time of this ListSecurityDataClassificationRulesRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListSecurityDataClassificationRulesRequest.

        结束日期

        :param end_time: The end_time of this ListSecurityDataClassificationRulesRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def order_by(self):
        r"""Gets the order_by of this ListSecurityDataClassificationRulesRequest.

        排序字段, createdAt, createdBy, updatedAt, updatedBy, name, description

        :return: The order_by of this ListSecurityDataClassificationRulesRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListSecurityDataClassificationRulesRequest.

        排序字段, createdAt, createdBy, updatedAt, updatedBy, name, description

        :param order_by: The order_by of this ListSecurityDataClassificationRulesRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def desc(self):
        r"""Gets the desc of this ListSecurityDataClassificationRulesRequest.

        排序规则

        :return: The desc of this ListSecurityDataClassificationRulesRequest.
        :rtype: bool
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this ListSecurityDataClassificationRulesRequest.

        排序规则

        :param desc: The desc of this ListSecurityDataClassificationRulesRequest.
        :type desc: bool
        """
        self._desc = desc

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
        if not isinstance(other, ListSecurityDataClassificationRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
