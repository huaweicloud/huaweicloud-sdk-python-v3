# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MindmapRecyclePageParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'creator_num': 'str',
        'limit': 'int',
        'offset': 'int',
        'project_id': 'str',
        'text': 'str'
    }

    attribute_map = {
        'creator_num': 'creator_num',
        'limit': 'limit',
        'offset': 'offset',
        'project_id': 'project_id',
        'text': 'text'
    }

    def __init__(self, creator_num=None, limit=None, offset=None, project_id=None, text=None):
        r"""MindmapRecyclePageParam

        The model defined in huaweicloud sdk

        :param creator_num: 创建人工号
        :type creator_num: str
        :param limit: 每页显示的条目数量，最大支持200条
        :type limit: int
        :param offset: 起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于100000
        :type offset: int
        :param project_id: 项目ID
        :type project_id: str
        :param text: 过滤用字段
        :type text: str
        """
        
        

        self._creator_num = None
        self._limit = None
        self._offset = None
        self._project_id = None
        self._text = None
        self.discriminator = None

        if creator_num is not None:
            self.creator_num = creator_num
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if project_id is not None:
            self.project_id = project_id
        if text is not None:
            self.text = text

    @property
    def creator_num(self):
        r"""Gets the creator_num of this MindmapRecyclePageParam.

        创建人工号

        :return: The creator_num of this MindmapRecyclePageParam.
        :rtype: str
        """
        return self._creator_num

    @creator_num.setter
    def creator_num(self, creator_num):
        r"""Sets the creator_num of this MindmapRecyclePageParam.

        创建人工号

        :param creator_num: The creator_num of this MindmapRecyclePageParam.
        :type creator_num: str
        """
        self._creator_num = creator_num

    @property
    def limit(self):
        r"""Gets the limit of this MindmapRecyclePageParam.

        每页显示的条目数量，最大支持200条

        :return: The limit of this MindmapRecyclePageParam.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this MindmapRecyclePageParam.

        每页显示的条目数量，最大支持200条

        :param limit: The limit of this MindmapRecyclePageParam.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this MindmapRecyclePageParam.

        起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于100000

        :return: The offset of this MindmapRecyclePageParam.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this MindmapRecyclePageParam.

        起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于100000

        :param offset: The offset of this MindmapRecyclePageParam.
        :type offset: int
        """
        self._offset = offset

    @property
    def project_id(self):
        r"""Gets the project_id of this MindmapRecyclePageParam.

        项目ID

        :return: The project_id of this MindmapRecyclePageParam.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this MindmapRecyclePageParam.

        项目ID

        :param project_id: The project_id of this MindmapRecyclePageParam.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def text(self):
        r"""Gets the text of this MindmapRecyclePageParam.

        过滤用字段

        :return: The text of this MindmapRecyclePageParam.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        r"""Sets the text of this MindmapRecyclePageParam.

        过滤用字段

        :param text: The text of this MindmapRecyclePageParam.
        :type text: str
        """
        self._text = text

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
        if not isinstance(other, MindmapRecyclePageParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
