# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Job:

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
        'create_time': 'int',
        'create_by': 'str',
        'update_time': 'int',
        'update_by': 'str',
        'description': 'str',
        'enterprise_project_id': 'str',
        'project_id': 'str',
        'steps': 'list[Step]',
        'parameters': 'list[Parameter]',
        'rate_control': 'RateControl',
        'approve_info': 'ApproveInfo'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'create_time': 'create_time',
        'create_by': 'create_by',
        'update_time': 'update_time',
        'update_by': 'update_by',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'project_id': 'project_id',
        'steps': 'steps',
        'parameters': 'parameters',
        'rate_control': 'rate_control',
        'approve_info': 'approve_info'
    }

    def __init__(self, id=None, name=None, create_time=None, create_by=None, update_time=None, update_by=None, description=None, enterprise_project_id=None, project_id=None, steps=None, parameters=None, rate_control=None, approve_info=None):
        """Job

        The model defined in huaweicloud sdk

        :param id: 作业id。
        :type id: str
        :param name: 作业名称。
        :type name: str
        :param create_time: 实体的创建时间戳。
        :type create_time: int
        :param create_by: 创建人。
        :type create_by: str
        :param update_time: 实体的最后更新时间戳。 注意：执行创建/修补/删除操作时，update_time将更新。
        :type update_time: int
        :param update_by: 修改人。
        :type update_by: str
        :param description: 作业描述,对脚本进行描述，最大长度为1000。
        :type description: str
        :param enterprise_project_id: 企业项目id。
        :type enterprise_project_id: str
        :param project_id: 租户从IAM申请到的projectid，一般为32位字符串。
        :type project_id: str
        :param steps: 作业步骤。
        :type steps: list[:class:`huaweicloudsdkaom.v1.Step`]
        :param parameters: 全局参数。
        :type parameters: list[:class:`huaweicloudsdkaom.v1.Parameter`]
        :param rate_control: 
        :type rate_control: :class:`huaweicloudsdkaom.v1.RateControl`
        :param approve_info: 
        :type approve_info: :class:`huaweicloudsdkaom.v1.ApproveInfo`
        """
        
        

        self._id = None
        self._name = None
        self._create_time = None
        self._create_by = None
        self._update_time = None
        self._update_by = None
        self._description = None
        self._enterprise_project_id = None
        self._project_id = None
        self._steps = None
        self._parameters = None
        self._rate_control = None
        self._approve_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if create_time is not None:
            self.create_time = create_time
        if create_by is not None:
            self.create_by = create_by
        if update_time is not None:
            self.update_time = update_time
        if update_by is not None:
            self.update_by = update_by
        if description is not None:
            self.description = description
        self.enterprise_project_id = enterprise_project_id
        self.project_id = project_id
        self.steps = steps
        self.parameters = parameters
        self.rate_control = rate_control
        self.approve_info = approve_info

    @property
    def id(self):
        """Gets the id of this Job.

        作业id。

        :return: The id of this Job.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Job.

        作业id。

        :param id: The id of this Job.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Job.

        作业名称。

        :return: The name of this Job.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Job.

        作业名称。

        :param name: The name of this Job.
        :type name: str
        """
        self._name = name

    @property
    def create_time(self):
        """Gets the create_time of this Job.

        实体的创建时间戳。

        :return: The create_time of this Job.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Job.

        实体的创建时间戳。

        :param create_time: The create_time of this Job.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def create_by(self):
        """Gets the create_by of this Job.

        创建人。

        :return: The create_by of this Job.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this Job.

        创建人。

        :param create_by: The create_by of this Job.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_time(self):
        """Gets the update_time of this Job.

        实体的最后更新时间戳。 注意：执行创建/修补/删除操作时，update_time将更新。

        :return: The update_time of this Job.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Job.

        实体的最后更新时间戳。 注意：执行创建/修补/删除操作时，update_time将更新。

        :param update_time: The update_time of this Job.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def update_by(self):
        """Gets the update_by of this Job.

        修改人。

        :return: The update_by of this Job.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        """Sets the update_by of this Job.

        修改人。

        :param update_by: The update_by of this Job.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def description(self):
        """Gets the description of this Job.

        作业描述,对脚本进行描述，最大长度为1000。

        :return: The description of this Job.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Job.

        作业描述,对脚本进行描述，最大长度为1000。

        :param description: The description of this Job.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this Job.

        企业项目id。

        :return: The enterprise_project_id of this Job.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this Job.

        企业项目id。

        :param enterprise_project_id: The enterprise_project_id of this Job.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def project_id(self):
        """Gets the project_id of this Job.

        租户从IAM申请到的projectid，一般为32位字符串。

        :return: The project_id of this Job.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Job.

        租户从IAM申请到的projectid，一般为32位字符串。

        :param project_id: The project_id of this Job.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def steps(self):
        """Gets the steps of this Job.

        作业步骤。

        :return: The steps of this Job.
        :rtype: list[:class:`huaweicloudsdkaom.v1.Step`]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this Job.

        作业步骤。

        :param steps: The steps of this Job.
        :type steps: list[:class:`huaweicloudsdkaom.v1.Step`]
        """
        self._steps = steps

    @property
    def parameters(self):
        """Gets the parameters of this Job.

        全局参数。

        :return: The parameters of this Job.
        :rtype: list[:class:`huaweicloudsdkaom.v1.Parameter`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this Job.

        全局参数。

        :param parameters: The parameters of this Job.
        :type parameters: list[:class:`huaweicloudsdkaom.v1.Parameter`]
        """
        self._parameters = parameters

    @property
    def rate_control(self):
        """Gets the rate_control of this Job.

        :return: The rate_control of this Job.
        :rtype: :class:`huaweicloudsdkaom.v1.RateControl`
        """
        return self._rate_control

    @rate_control.setter
    def rate_control(self, rate_control):
        """Sets the rate_control of this Job.

        :param rate_control: The rate_control of this Job.
        :type rate_control: :class:`huaweicloudsdkaom.v1.RateControl`
        """
        self._rate_control = rate_control

    @property
    def approve_info(self):
        """Gets the approve_info of this Job.

        :return: The approve_info of this Job.
        :rtype: :class:`huaweicloudsdkaom.v1.ApproveInfo`
        """
        return self._approve_info

    @approve_info.setter
    def approve_info(self, approve_info):
        """Sets the approve_info of this Job.

        :param approve_info: The approve_info of this Job.
        :type approve_info: :class:`huaweicloudsdkaom.v1.ApproveInfo`
        """
        self._approve_info = approve_info

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
        if not isinstance(other, Job):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
