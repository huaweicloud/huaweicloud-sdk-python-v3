# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StudyRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'id': 'str',
        'eihealth_project_name': 'str',
        'eihealth_project_id': 'str',
        'description': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'latest_job': 'StudyJobRsp'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'eihealth_project_name': 'eihealth_project_name',
        'eihealth_project_id': 'eihealth_project_id',
        'description': 'description',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'latest_job': 'latest_job'
    }

    def __init__(self, name=None, id=None, eihealth_project_name=None, eihealth_project_id=None, description=None, create_time=None, update_time=None, latest_job=None):
        r"""StudyRsp

        The model defined in huaweicloud sdk

        :param name: study名称
        :type name: str
        :param id: study id
        :type id: str
        :param eihealth_project_name: 医疗项目名称
        :type eihealth_project_name: str
        :param eihealth_project_id: 医疗项目id
        :type eihealth_project_id: str
        :param description: study描述
        :type description: str
        :param create_time: study创建时间
        :type create_time: str
        :param update_time: study更新时间
        :type update_time: str
        :param latest_job: 
        :type latest_job: :class:`huaweicloudsdkeihealth.v1.StudyJobRsp`
        """
        
        

        self._name = None
        self._id = None
        self._eihealth_project_name = None
        self._eihealth_project_id = None
        self._description = None
        self._create_time = None
        self._update_time = None
        self._latest_job = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if eihealth_project_name is not None:
            self.eihealth_project_name = eihealth_project_name
        if eihealth_project_id is not None:
            self.eihealth_project_id = eihealth_project_id
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if latest_job is not None:
            self.latest_job = latest_job

    @property
    def name(self):
        r"""Gets the name of this StudyRsp.

        study名称

        :return: The name of this StudyRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this StudyRsp.

        study名称

        :param name: The name of this StudyRsp.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this StudyRsp.

        study id

        :return: The id of this StudyRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this StudyRsp.

        study id

        :param id: The id of this StudyRsp.
        :type id: str
        """
        self._id = id

    @property
    def eihealth_project_name(self):
        r"""Gets the eihealth_project_name of this StudyRsp.

        医疗项目名称

        :return: The eihealth_project_name of this StudyRsp.
        :rtype: str
        """
        return self._eihealth_project_name

    @eihealth_project_name.setter
    def eihealth_project_name(self, eihealth_project_name):
        r"""Sets the eihealth_project_name of this StudyRsp.

        医疗项目名称

        :param eihealth_project_name: The eihealth_project_name of this StudyRsp.
        :type eihealth_project_name: str
        """
        self._eihealth_project_name = eihealth_project_name

    @property
    def eihealth_project_id(self):
        r"""Gets the eihealth_project_id of this StudyRsp.

        医疗项目id

        :return: The eihealth_project_id of this StudyRsp.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        r"""Sets the eihealth_project_id of this StudyRsp.

        医疗项目id

        :param eihealth_project_id: The eihealth_project_id of this StudyRsp.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def description(self):
        r"""Gets the description of this StudyRsp.

        study描述

        :return: The description of this StudyRsp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this StudyRsp.

        study描述

        :param description: The description of this StudyRsp.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this StudyRsp.

        study创建时间

        :return: The create_time of this StudyRsp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this StudyRsp.

        study创建时间

        :param create_time: The create_time of this StudyRsp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this StudyRsp.

        study更新时间

        :return: The update_time of this StudyRsp.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this StudyRsp.

        study更新时间

        :param update_time: The update_time of this StudyRsp.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def latest_job(self):
        r"""Gets the latest_job of this StudyRsp.

        :return: The latest_job of this StudyRsp.
        :rtype: :class:`huaweicloudsdkeihealth.v1.StudyJobRsp`
        """
        return self._latest_job

    @latest_job.setter
    def latest_job(self, latest_job):
        r"""Sets the latest_job of this StudyRsp.

        :param latest_job: The latest_job of this StudyRsp.
        :type latest_job: :class:`huaweicloudsdkeihealth.v1.StudyJobRsp`
        """
        self._latest_job = latest_job

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
        if not isinstance(other, StudyRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
