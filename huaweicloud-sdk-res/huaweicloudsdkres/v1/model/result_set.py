# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResultSet:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability': 'int',
        'category': 'str',
        'job_id': 'str',
        'job_type': 'str',
        'rec_id': 'str',
        'rec_type': 'str',
        'scene_id': 'str',
        'table_name': 'str',
        'workspace_id': 'str'
    }

    attribute_map = {
        'availability': 'availability',
        'category': 'category',
        'job_id': 'job_id',
        'job_type': 'job_type',
        'rec_id': 'rec_id',
        'rec_type': 'rec_type',
        'scene_id': 'scene_id',
        'table_name': 'table_name',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, availability=None, category=None, job_id=None, job_type=None, rec_id=None, rec_type=None, scene_id=None, table_name=None, workspace_id=None):
        """ResultSet

        The model defined in huaweicloud sdk

        :param availability: 可用性
        :type availability: int
        :param category: 类别
        :type category: str
        :param job_id: 作业编号
        :type job_id: str
        :param job_type: 作业类型
        :type job_type: str
        :param rec_id: rec编号
        :type rec_id: str
        :param rec_type: rec类型
        :type rec_type: str
        :param scene_id: 场景编号
        :type scene_id: str
        :param table_name: 表名
        :type table_name: str
        :param workspace_id: 工作空间编号
        :type workspace_id: str
        """
        
        

        self._availability = None
        self._category = None
        self._job_id = None
        self._job_type = None
        self._rec_id = None
        self._rec_type = None
        self._scene_id = None
        self._table_name = None
        self._workspace_id = None
        self.discriminator = None

        if availability is not None:
            self.availability = availability
        if category is not None:
            self.category = category
        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
        if rec_id is not None:
            self.rec_id = rec_id
        if rec_type is not None:
            self.rec_type = rec_type
        if scene_id is not None:
            self.scene_id = scene_id
        if table_name is not None:
            self.table_name = table_name
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def availability(self):
        """Gets the availability of this ResultSet.

        可用性

        :return: The availability of this ResultSet.
        :rtype: int
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this ResultSet.

        可用性

        :param availability: The availability of this ResultSet.
        :type availability: int
        """
        self._availability = availability

    @property
    def category(self):
        """Gets the category of this ResultSet.

        类别

        :return: The category of this ResultSet.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ResultSet.

        类别

        :param category: The category of this ResultSet.
        :type category: str
        """
        self._category = category

    @property
    def job_id(self):
        """Gets the job_id of this ResultSet.

        作业编号

        :return: The job_id of this ResultSet.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ResultSet.

        作业编号

        :param job_id: The job_id of this ResultSet.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        """Gets the job_type of this ResultSet.

        作业类型

        :return: The job_type of this ResultSet.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this ResultSet.

        作业类型

        :param job_type: The job_type of this ResultSet.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def rec_id(self):
        """Gets the rec_id of this ResultSet.

        rec编号

        :return: The rec_id of this ResultSet.
        :rtype: str
        """
        return self._rec_id

    @rec_id.setter
    def rec_id(self, rec_id):
        """Sets the rec_id of this ResultSet.

        rec编号

        :param rec_id: The rec_id of this ResultSet.
        :type rec_id: str
        """
        self._rec_id = rec_id

    @property
    def rec_type(self):
        """Gets the rec_type of this ResultSet.

        rec类型

        :return: The rec_type of this ResultSet.
        :rtype: str
        """
        return self._rec_type

    @rec_type.setter
    def rec_type(self, rec_type):
        """Sets the rec_type of this ResultSet.

        rec类型

        :param rec_type: The rec_type of this ResultSet.
        :type rec_type: str
        """
        self._rec_type = rec_type

    @property
    def scene_id(self):
        """Gets the scene_id of this ResultSet.

        场景编号

        :return: The scene_id of this ResultSet.
        :rtype: str
        """
        return self._scene_id

    @scene_id.setter
    def scene_id(self, scene_id):
        """Sets the scene_id of this ResultSet.

        场景编号

        :param scene_id: The scene_id of this ResultSet.
        :type scene_id: str
        """
        self._scene_id = scene_id

    @property
    def table_name(self):
        """Gets the table_name of this ResultSet.

        表名

        :return: The table_name of this ResultSet.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this ResultSet.

        表名

        :param table_name: The table_name of this ResultSet.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ResultSet.

        工作空间编号

        :return: The workspace_id of this ResultSet.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ResultSet.

        工作空间编号

        :param workspace_id: The workspace_id of this ResultSet.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

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
        if not isinstance(other, ResultSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
