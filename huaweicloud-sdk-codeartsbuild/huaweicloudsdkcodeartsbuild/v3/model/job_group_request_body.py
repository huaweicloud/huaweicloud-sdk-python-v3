# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobGroupRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'project_id': 'str',
        'parent_id': 'str',
        'group_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'parent_id': 'parent_id',
        'group_id': 'group_id'
    }

    def __init__(self, id=None, name=None, project_id=None, parent_id=None, group_id=None):
        r"""JobGroupRequestBody

        The model defined in huaweicloud sdk

        :param id: 主键id
        :type id: str
        :param name: 分组名称
        :type name: str
        :param project_id: CodeArts项目ID。获取方式请参考[获取CodeArts项目ID](https://support.huaweicloud.com/api-codeci/cloudbuild_03_0022.html)。
        :type project_id: str
        :param parent_id: 父分组id
        :type parent_id: str
        :param group_id: 任务分组id
        :type group_id: str
        """
        
        

        self._id = None
        self._name = None
        self._project_id = None
        self._parent_id = None
        self._group_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if parent_id is not None:
            self.parent_id = parent_id
        if group_id is not None:
            self.group_id = group_id

    @property
    def id(self):
        r"""Gets the id of this JobGroupRequestBody.

        主键id

        :return: The id of this JobGroupRequestBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this JobGroupRequestBody.

        主键id

        :param id: The id of this JobGroupRequestBody.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this JobGroupRequestBody.

        分组名称

        :return: The name of this JobGroupRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this JobGroupRequestBody.

        分组名称

        :param name: The name of this JobGroupRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this JobGroupRequestBody.

        CodeArts项目ID。获取方式请参考[获取CodeArts项目ID](https://support.huaweicloud.com/api-codeci/cloudbuild_03_0022.html)。

        :return: The project_id of this JobGroupRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this JobGroupRequestBody.

        CodeArts项目ID。获取方式请参考[获取CodeArts项目ID](https://support.huaweicloud.com/api-codeci/cloudbuild_03_0022.html)。

        :param project_id: The project_id of this JobGroupRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def parent_id(self):
        r"""Gets the parent_id of this JobGroupRequestBody.

        父分组id

        :return: The parent_id of this JobGroupRequestBody.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this JobGroupRequestBody.

        父分组id

        :param parent_id: The parent_id of this JobGroupRequestBody.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def group_id(self):
        r"""Gets the group_id of this JobGroupRequestBody.

        任务分组id

        :return: The group_id of this JobGroupRequestBody.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this JobGroupRequestBody.

        任务分组id

        :param group_id: The group_id of this JobGroupRequestBody.
        :type group_id: str
        """
        self._group_id = group_id

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
        if not isinstance(other, JobGroupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
