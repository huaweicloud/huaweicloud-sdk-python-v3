# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskResultVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uri': 'str',
        'name': 'str',
        'task_uri': 'str',
        'description': 'str',
        'owner': 'str',
        'owner_name': 'str',
        'release_dev': 'str',
        'version_uri': 'str',
        'creator': 'str',
        'creator_name': 'str',
        'create_time': 'str',
        'updator': 'str',
        'updator_name': 'str',
        'update_time': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'result_name': 'str',
        'project_uuid': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'task_uri': 'task_uri',
        'description': 'description',
        'owner': 'owner',
        'owner_name': 'owner_name',
        'release_dev': 'release_dev',
        'version_uri': 'version_uri',
        'creator': 'creator',
        'creator_name': 'creator_name',
        'create_time': 'create_time',
        'updator': 'updator',
        'updator_name': 'updator_name',
        'update_time': 'update_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'result_name': 'result_name',
        'project_uuid': 'project_uuid'
    }

    def __init__(self, uri=None, name=None, task_uri=None, description=None, owner=None, owner_name=None, release_dev=None, version_uri=None, creator=None, creator_name=None, create_time=None, updator=None, updator_name=None, update_time=None, start_time=None, end_time=None, result_name=None, project_uuid=None):
        r"""TaskResultVo

        The model defined in huaweicloud sdk

        :param uri: 结果URI
        :type uri: str
        :param name: 测试套名称
        :type name: str
        :param task_uri: 任务uri
        :type task_uri: str
        :param description: 描述
        :type description: str
        :param owner: 责任人
        :type owner: str
        :param owner_name: 责任人名称
        :type owner_name: str
        :param release_dev: 发布版本号
        :type release_dev: str
        :param version_uri: 分支/迭代uri
        :type version_uri: str
        :param creator: 创建人id
        :type creator: str
        :param creator_name: 创建人名称
        :type creator_name: str
        :param create_time: 创建时间
        :type create_time: str
        :param updator: 更新人
        :type updator: str
        :param updator_name: 更新人名称
        :type updator_name: str
        :param update_time: 更新人名称
        :type update_time: str
        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param result_name: 测试结果名称
        :type result_name: str
        :param project_uuid: 项目id
        :type project_uuid: str
        """
        
        

        self._uri = None
        self._name = None
        self._task_uri = None
        self._description = None
        self._owner = None
        self._owner_name = None
        self._release_dev = None
        self._version_uri = None
        self._creator = None
        self._creator_name = None
        self._create_time = None
        self._updator = None
        self._updator_name = None
        self._update_time = None
        self._start_time = None
        self._end_time = None
        self._result_name = None
        self._project_uuid = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if name is not None:
            self.name = name
        if task_uri is not None:
            self.task_uri = task_uri
        if description is not None:
            self.description = description
        if owner is not None:
            self.owner = owner
        if owner_name is not None:
            self.owner_name = owner_name
        if release_dev is not None:
            self.release_dev = release_dev
        if version_uri is not None:
            self.version_uri = version_uri
        if creator is not None:
            self.creator = creator
        if creator_name is not None:
            self.creator_name = creator_name
        if create_time is not None:
            self.create_time = create_time
        if updator is not None:
            self.updator = updator
        if updator_name is not None:
            self.updator_name = updator_name
        if update_time is not None:
            self.update_time = update_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if result_name is not None:
            self.result_name = result_name
        if project_uuid is not None:
            self.project_uuid = project_uuid

    @property
    def uri(self):
        r"""Gets the uri of this TaskResultVo.

        结果URI

        :return: The uri of this TaskResultVo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this TaskResultVo.

        结果URI

        :param uri: The uri of this TaskResultVo.
        :type uri: str
        """
        self._uri = uri

    @property
    def name(self):
        r"""Gets the name of this TaskResultVo.

        测试套名称

        :return: The name of this TaskResultVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TaskResultVo.

        测试套名称

        :param name: The name of this TaskResultVo.
        :type name: str
        """
        self._name = name

    @property
    def task_uri(self):
        r"""Gets the task_uri of this TaskResultVo.

        任务uri

        :return: The task_uri of this TaskResultVo.
        :rtype: str
        """
        return self._task_uri

    @task_uri.setter
    def task_uri(self, task_uri):
        r"""Sets the task_uri of this TaskResultVo.

        任务uri

        :param task_uri: The task_uri of this TaskResultVo.
        :type task_uri: str
        """
        self._task_uri = task_uri

    @property
    def description(self):
        r"""Gets the description of this TaskResultVo.

        描述

        :return: The description of this TaskResultVo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TaskResultVo.

        描述

        :param description: The description of this TaskResultVo.
        :type description: str
        """
        self._description = description

    @property
    def owner(self):
        r"""Gets the owner of this TaskResultVo.

        责任人

        :return: The owner of this TaskResultVo.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this TaskResultVo.

        责任人

        :param owner: The owner of this TaskResultVo.
        :type owner: str
        """
        self._owner = owner

    @property
    def owner_name(self):
        r"""Gets the owner_name of this TaskResultVo.

        责任人名称

        :return: The owner_name of this TaskResultVo.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        r"""Sets the owner_name of this TaskResultVo.

        责任人名称

        :param owner_name: The owner_name of this TaskResultVo.
        :type owner_name: str
        """
        self._owner_name = owner_name

    @property
    def release_dev(self):
        r"""Gets the release_dev of this TaskResultVo.

        发布版本号

        :return: The release_dev of this TaskResultVo.
        :rtype: str
        """
        return self._release_dev

    @release_dev.setter
    def release_dev(self, release_dev):
        r"""Sets the release_dev of this TaskResultVo.

        发布版本号

        :param release_dev: The release_dev of this TaskResultVo.
        :type release_dev: str
        """
        self._release_dev = release_dev

    @property
    def version_uri(self):
        r"""Gets the version_uri of this TaskResultVo.

        分支/迭代uri

        :return: The version_uri of this TaskResultVo.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        r"""Sets the version_uri of this TaskResultVo.

        分支/迭代uri

        :param version_uri: The version_uri of this TaskResultVo.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def creator(self):
        r"""Gets the creator of this TaskResultVo.

        创建人id

        :return: The creator of this TaskResultVo.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this TaskResultVo.

        创建人id

        :param creator: The creator of this TaskResultVo.
        :type creator: str
        """
        self._creator = creator

    @property
    def creator_name(self):
        r"""Gets the creator_name of this TaskResultVo.

        创建人名称

        :return: The creator_name of this TaskResultVo.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this TaskResultVo.

        创建人名称

        :param creator_name: The creator_name of this TaskResultVo.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def create_time(self):
        r"""Gets the create_time of this TaskResultVo.

        创建时间

        :return: The create_time of this TaskResultVo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TaskResultVo.

        创建时间

        :param create_time: The create_time of this TaskResultVo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def updator(self):
        r"""Gets the updator of this TaskResultVo.

        更新人

        :return: The updator of this TaskResultVo.
        :rtype: str
        """
        return self._updator

    @updator.setter
    def updator(self, updator):
        r"""Sets the updator of this TaskResultVo.

        更新人

        :param updator: The updator of this TaskResultVo.
        :type updator: str
        """
        self._updator = updator

    @property
    def updator_name(self):
        r"""Gets the updator_name of this TaskResultVo.

        更新人名称

        :return: The updator_name of this TaskResultVo.
        :rtype: str
        """
        return self._updator_name

    @updator_name.setter
    def updator_name(self, updator_name):
        r"""Sets the updator_name of this TaskResultVo.

        更新人名称

        :param updator_name: The updator_name of this TaskResultVo.
        :type updator_name: str
        """
        self._updator_name = updator_name

    @property
    def update_time(self):
        r"""Gets the update_time of this TaskResultVo.

        更新人名称

        :return: The update_time of this TaskResultVo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this TaskResultVo.

        更新人名称

        :param update_time: The update_time of this TaskResultVo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def start_time(self):
        r"""Gets the start_time of this TaskResultVo.

        开始时间

        :return: The start_time of this TaskResultVo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this TaskResultVo.

        开始时间

        :param start_time: The start_time of this TaskResultVo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this TaskResultVo.

        结束时间

        :return: The end_time of this TaskResultVo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this TaskResultVo.

        结束时间

        :param end_time: The end_time of this TaskResultVo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def result_name(self):
        r"""Gets the result_name of this TaskResultVo.

        测试结果名称

        :return: The result_name of this TaskResultVo.
        :rtype: str
        """
        return self._result_name

    @result_name.setter
    def result_name(self, result_name):
        r"""Sets the result_name of this TaskResultVo.

        测试结果名称

        :param result_name: The result_name of this TaskResultVo.
        :type result_name: str
        """
        self._result_name = result_name

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this TaskResultVo.

        项目id

        :return: The project_uuid of this TaskResultVo.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this TaskResultVo.

        项目id

        :param project_uuid: The project_uuid of this TaskResultVo.
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
        if not isinstance(other, TaskResultVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
