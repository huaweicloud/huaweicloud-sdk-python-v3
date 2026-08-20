# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SprintSnapshotsCreateParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'title': 'str',
        'issue_id': 'str',
        'category': 'str'
    }

    attribute_map = {
        'title': 'title',
        'issue_id': 'issue_id',
        'category': 'category'
    }

    def __init__(self, title=None, issue_id=None, category=None):
        r"""SprintSnapshotsCreateParam

        The model defined in huaweicloud sdk

        :param title: 快照标题。
        :type title: str
        :param issue_id: 计划唯一ID。可以通过IPD项目计划管理章节中发布/迭代计划列表查询接口获取，响应消息体中的id字段的值就是计划ID。
        :type issue_id: str
        :param category: 计划类别。可以通过IPD项目计划管理章节中发布/迭代计划列表查询接口获取，响应消息体中的category字段的值就是计划类别。
        :type category: str
        """
        
        

        self._title = None
        self._issue_id = None
        self._category = None
        self.discriminator = None

        self.title = title
        self.issue_id = issue_id
        self.category = category

    @property
    def title(self):
        r"""Gets the title of this SprintSnapshotsCreateParam.

        快照标题。

        :return: The title of this SprintSnapshotsCreateParam.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this SprintSnapshotsCreateParam.

        快照标题。

        :param title: The title of this SprintSnapshotsCreateParam.
        :type title: str
        """
        self._title = title

    @property
    def issue_id(self):
        r"""Gets the issue_id of this SprintSnapshotsCreateParam.

        计划唯一ID。可以通过IPD项目计划管理章节中发布/迭代计划列表查询接口获取，响应消息体中的id字段的值就是计划ID。

        :return: The issue_id of this SprintSnapshotsCreateParam.
        :rtype: str
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        r"""Sets the issue_id of this SprintSnapshotsCreateParam.

        计划唯一ID。可以通过IPD项目计划管理章节中发布/迭代计划列表查询接口获取，响应消息体中的id字段的值就是计划ID。

        :param issue_id: The issue_id of this SprintSnapshotsCreateParam.
        :type issue_id: str
        """
        self._issue_id = issue_id

    @property
    def category(self):
        r"""Gets the category of this SprintSnapshotsCreateParam.

        计划类别。可以通过IPD项目计划管理章节中发布/迭代计划列表查询接口获取，响应消息体中的category字段的值就是计划类别。

        :return: The category of this SprintSnapshotsCreateParam.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this SprintSnapshotsCreateParam.

        计划类别。可以通过IPD项目计划管理章节中发布/迭代计划列表查询接口获取，响应消息体中的category字段的值就是计划类别。

        :param category: The category of this SprintSnapshotsCreateParam.
        :type category: str
        """
        self._category = category

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SprintSnapshotsCreateParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
