# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddRelationsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'relations': 'list[RelationInfo]',
        'tracker_id': 'str',
        'version_uri': 'str',
        'task_uri': 'str',
        'add_to_iterator': 'bool',
        'project_uuid': 'str'
    }

    attribute_map = {
        'relations': 'relations',
        'tracker_id': 'tracker_id',
        'version_uri': 'version_uri',
        'task_uri': 'task_uri',
        'add_to_iterator': 'add_to_iterator',
        'project_uuid': 'project_uuid'
    }

    def __init__(self, relations=None, tracker_id=None, version_uri=None, task_uri=None, add_to_iterator=None, project_uuid=None):
        r"""AddRelationsInfo

        The model defined in huaweicloud sdk

        :param relations: 
        :type relations: list[:class:`huaweicloudsdkcloudtest.v1.RelationInfo`]
        :param tracker_id: 工作项类型id
        :type tracker_id: str
        :param version_uri: 版本uri
        :type version_uri: str
        :param task_uri: 测试套id
        :type task_uri: str
        :param add_to_iterator: 是否将需求添加到迭代
        :type add_to_iterator: bool
        :param project_uuid: 项目id
        :type project_uuid: str
        """
        
        

        self._relations = None
        self._tracker_id = None
        self._version_uri = None
        self._task_uri = None
        self._add_to_iterator = None
        self._project_uuid = None
        self.discriminator = None

        if relations is not None:
            self.relations = relations
        if tracker_id is not None:
            self.tracker_id = tracker_id
        if version_uri is not None:
            self.version_uri = version_uri
        if task_uri is not None:
            self.task_uri = task_uri
        if add_to_iterator is not None:
            self.add_to_iterator = add_to_iterator
        if project_uuid is not None:
            self.project_uuid = project_uuid

    @property
    def relations(self):
        r"""Gets the relations of this AddRelationsInfo.

        :return: The relations of this AddRelationsInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.RelationInfo`]
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        r"""Sets the relations of this AddRelationsInfo.

        :param relations: The relations of this AddRelationsInfo.
        :type relations: list[:class:`huaweicloudsdkcloudtest.v1.RelationInfo`]
        """
        self._relations = relations

    @property
    def tracker_id(self):
        r"""Gets the tracker_id of this AddRelationsInfo.

        工作项类型id

        :return: The tracker_id of this AddRelationsInfo.
        :rtype: str
        """
        return self._tracker_id

    @tracker_id.setter
    def tracker_id(self, tracker_id):
        r"""Sets the tracker_id of this AddRelationsInfo.

        工作项类型id

        :param tracker_id: The tracker_id of this AddRelationsInfo.
        :type tracker_id: str
        """
        self._tracker_id = tracker_id

    @property
    def version_uri(self):
        r"""Gets the version_uri of this AddRelationsInfo.

        版本uri

        :return: The version_uri of this AddRelationsInfo.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        r"""Sets the version_uri of this AddRelationsInfo.

        版本uri

        :param version_uri: The version_uri of this AddRelationsInfo.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def task_uri(self):
        r"""Gets the task_uri of this AddRelationsInfo.

        测试套id

        :return: The task_uri of this AddRelationsInfo.
        :rtype: str
        """
        return self._task_uri

    @task_uri.setter
    def task_uri(self, task_uri):
        r"""Sets the task_uri of this AddRelationsInfo.

        测试套id

        :param task_uri: The task_uri of this AddRelationsInfo.
        :type task_uri: str
        """
        self._task_uri = task_uri

    @property
    def add_to_iterator(self):
        r"""Gets the add_to_iterator of this AddRelationsInfo.

        是否将需求添加到迭代

        :return: The add_to_iterator of this AddRelationsInfo.
        :rtype: bool
        """
        return self._add_to_iterator

    @add_to_iterator.setter
    def add_to_iterator(self, add_to_iterator):
        r"""Sets the add_to_iterator of this AddRelationsInfo.

        是否将需求添加到迭代

        :param add_to_iterator: The add_to_iterator of this AddRelationsInfo.
        :type add_to_iterator: bool
        """
        self._add_to_iterator = add_to_iterator

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this AddRelationsInfo.

        项目id

        :return: The project_uuid of this AddRelationsInfo.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this AddRelationsInfo.

        项目id

        :param project_uuid: The project_uuid of this AddRelationsInfo.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

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
        if not isinstance(other, AddRelationsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
