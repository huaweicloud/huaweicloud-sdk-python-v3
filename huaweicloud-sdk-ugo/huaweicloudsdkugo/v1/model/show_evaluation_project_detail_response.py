# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEvaluationProjectDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'source_db_size': 'str',
        'source_db_schema': 'int',
        'source_db_cpu': 'str',
        'source_db_character_set': 'str',
        'source_db_os': 'str',
        'source_db_instance_num': 'int',
        'source_db_ram': 'str',
        'source_db_info': 'SourceDB',
        'source_db_phy_ram': 'str',
        'source_db_version': 'str',
        'source_db_conf': 'str',
        'source_db_clock': 'str',
        'evaluation_project_id': 'int',
        'evaluation_project_name': 'str'
    }

    attribute_map = {
        'source_db_size': 'source_db_size',
        'source_db_schema': 'source_db_schema',
        'source_db_cpu': 'source_db_cpu',
        'source_db_character_set': 'source_db_character_set',
        'source_db_os': 'source_db_os',
        'source_db_instance_num': 'source_db_instance_num',
        'source_db_ram': 'source_db_ram',
        'source_db_info': 'source_db_info',
        'source_db_phy_ram': 'source_db_phy_ram',
        'source_db_version': 'source_db_version',
        'source_db_conf': 'source_db_conf',
        'source_db_clock': 'source_db_clock',
        'evaluation_project_id': 'evaluation_project_id',
        'evaluation_project_name': 'evaluation_project_name'
    }

    def __init__(self, source_db_size=None, source_db_schema=None, source_db_cpu=None, source_db_character_set=None, source_db_os=None, source_db_instance_num=None, source_db_ram=None, source_db_info=None, source_db_phy_ram=None, source_db_version=None, source_db_conf=None, source_db_clock=None, evaluation_project_id=None, evaluation_project_name=None):
        """ShowEvaluationProjectDetailResponse

        The model defined in huaweicloud sdk

        :param source_db_size: 数据库大小。
        :type source_db_size: str
        :param source_db_schema: 数据库schema个数。
        :type source_db_schema: int
        :param source_db_cpu: 数据库CPU个数。
        :type source_db_cpu: str
        :param source_db_character_set: 数据库字符集。
        :type source_db_character_set: str
        :param source_db_os: 数据库操作系统。
        :type source_db_os: str
        :param source_db_instance_num: 实例数量。
        :type source_db_instance_num: int
        :param source_db_ram: 数据库内存。
        :type source_db_ram: str
        :param source_db_info: 
        :type source_db_info: :class:`huaweicloudsdkugo.v1.SourceDB`
        :param source_db_phy_ram: 数据库物理RAM。
        :type source_db_phy_ram: str
        :param source_db_version: 数据库版本。
        :type source_db_version: str
        :param source_db_conf: 数据库配置。
        :type source_db_conf: str
        :param source_db_clock: 数据库时区。
        :type source_db_clock: str
        :param evaluation_project_id: 评估项目ID。
        :type evaluation_project_id: int
        :param evaluation_project_name: 评估项目名称。
        :type evaluation_project_name: str
        """
        
        super(ShowEvaluationProjectDetailResponse, self).__init__()

        self._source_db_size = None
        self._source_db_schema = None
        self._source_db_cpu = None
        self._source_db_character_set = None
        self._source_db_os = None
        self._source_db_instance_num = None
        self._source_db_ram = None
        self._source_db_info = None
        self._source_db_phy_ram = None
        self._source_db_version = None
        self._source_db_conf = None
        self._source_db_clock = None
        self._evaluation_project_id = None
        self._evaluation_project_name = None
        self.discriminator = None

        if source_db_size is not None:
            self.source_db_size = source_db_size
        if source_db_schema is not None:
            self.source_db_schema = source_db_schema
        if source_db_cpu is not None:
            self.source_db_cpu = source_db_cpu
        if source_db_character_set is not None:
            self.source_db_character_set = source_db_character_set
        if source_db_os is not None:
            self.source_db_os = source_db_os
        if source_db_instance_num is not None:
            self.source_db_instance_num = source_db_instance_num
        if source_db_ram is not None:
            self.source_db_ram = source_db_ram
        if source_db_info is not None:
            self.source_db_info = source_db_info
        if source_db_phy_ram is not None:
            self.source_db_phy_ram = source_db_phy_ram
        if source_db_version is not None:
            self.source_db_version = source_db_version
        if source_db_conf is not None:
            self.source_db_conf = source_db_conf
        if source_db_clock is not None:
            self.source_db_clock = source_db_clock
        if evaluation_project_id is not None:
            self.evaluation_project_id = evaluation_project_id
        if evaluation_project_name is not None:
            self.evaluation_project_name = evaluation_project_name

    @property
    def source_db_size(self):
        """Gets the source_db_size of this ShowEvaluationProjectDetailResponse.

        数据库大小。

        :return: The source_db_size of this ShowEvaluationProjectDetailResponse.
        :rtype: str
        """
        return self._source_db_size

    @source_db_size.setter
    def source_db_size(self, source_db_size):
        """Sets the source_db_size of this ShowEvaluationProjectDetailResponse.

        数据库大小。

        :param source_db_size: The source_db_size of this ShowEvaluationProjectDetailResponse.
        :type source_db_size: str
        """
        self._source_db_size = source_db_size

    @property
    def source_db_schema(self):
        """Gets the source_db_schema of this ShowEvaluationProjectDetailResponse.

        数据库schema个数。

        :return: The source_db_schema of this ShowEvaluationProjectDetailResponse.
        :rtype: int
        """
        return self._source_db_schema

    @source_db_schema.setter
    def source_db_schema(self, source_db_schema):
        """Sets the source_db_schema of this ShowEvaluationProjectDetailResponse.

        数据库schema个数。

        :param source_db_schema: The source_db_schema of this ShowEvaluationProjectDetailResponse.
        :type source_db_schema: int
        """
        self._source_db_schema = source_db_schema

    @property
    def source_db_cpu(self):
        """Gets the source_db_cpu of this ShowEvaluationProjectDetailResponse.

        数据库CPU个数。

        :return: The source_db_cpu of this ShowEvaluationProjectDetailResponse.
        :rtype: str
        """
        return self._source_db_cpu

    @source_db_cpu.setter
    def source_db_cpu(self, source_db_cpu):
        """Sets the source_db_cpu of this ShowEvaluationProjectDetailResponse.

        数据库CPU个数。

        :param source_db_cpu: The source_db_cpu of this ShowEvaluationProjectDetailResponse.
        :type source_db_cpu: str
        """
        self._source_db_cpu = source_db_cpu

    @property
    def source_db_character_set(self):
        """Gets the source_db_character_set of this ShowEvaluationProjectDetailResponse.

        数据库字符集。

        :return: The source_db_character_set of this ShowEvaluationProjectDetailResponse.
        :rtype: str
        """
        return self._source_db_character_set

    @source_db_character_set.setter
    def source_db_character_set(self, source_db_character_set):
        """Sets the source_db_character_set of this ShowEvaluationProjectDetailResponse.

        数据库字符集。

        :param source_db_character_set: The source_db_character_set of this ShowEvaluationProjectDetailResponse.
        :type source_db_character_set: str
        """
        self._source_db_character_set = source_db_character_set

    @property
    def source_db_os(self):
        """Gets the source_db_os of this ShowEvaluationProjectDetailResponse.

        数据库操作系统。

        :return: The source_db_os of this ShowEvaluationProjectDetailResponse.
        :rtype: str
        """
        return self._source_db_os

    @source_db_os.setter
    def source_db_os(self, source_db_os):
        """Sets the source_db_os of this ShowEvaluationProjectDetailResponse.

        数据库操作系统。

        :param source_db_os: The source_db_os of this ShowEvaluationProjectDetailResponse.
        :type source_db_os: str
        """
        self._source_db_os = source_db_os

    @property
    def source_db_instance_num(self):
        """Gets the source_db_instance_num of this ShowEvaluationProjectDetailResponse.

        实例数量。

        :return: The source_db_instance_num of this ShowEvaluationProjectDetailResponse.
        :rtype: int
        """
        return self._source_db_instance_num

    @source_db_instance_num.setter
    def source_db_instance_num(self, source_db_instance_num):
        """Sets the source_db_instance_num of this ShowEvaluationProjectDetailResponse.

        实例数量。

        :param source_db_instance_num: The source_db_instance_num of this ShowEvaluationProjectDetailResponse.
        :type source_db_instance_num: int
        """
        self._source_db_instance_num = source_db_instance_num

    @property
    def source_db_ram(self):
        """Gets the source_db_ram of this ShowEvaluationProjectDetailResponse.

        数据库内存。

        :return: The source_db_ram of this ShowEvaluationProjectDetailResponse.
        :rtype: str
        """
        return self._source_db_ram

    @source_db_ram.setter
    def source_db_ram(self, source_db_ram):
        """Sets the source_db_ram of this ShowEvaluationProjectDetailResponse.

        数据库内存。

        :param source_db_ram: The source_db_ram of this ShowEvaluationProjectDetailResponse.
        :type source_db_ram: str
        """
        self._source_db_ram = source_db_ram

    @property
    def source_db_info(self):
        """Gets the source_db_info of this ShowEvaluationProjectDetailResponse.


        :return: The source_db_info of this ShowEvaluationProjectDetailResponse.
        :rtype: :class:`huaweicloudsdkugo.v1.SourceDB`
        """
        return self._source_db_info

    @source_db_info.setter
    def source_db_info(self, source_db_info):
        """Sets the source_db_info of this ShowEvaluationProjectDetailResponse.


        :param source_db_info: The source_db_info of this ShowEvaluationProjectDetailResponse.
        :type source_db_info: :class:`huaweicloudsdkugo.v1.SourceDB`
        """
        self._source_db_info = source_db_info

    @property
    def source_db_phy_ram(self):
        """Gets the source_db_phy_ram of this ShowEvaluationProjectDetailResponse.

        数据库物理RAM。

        :return: The source_db_phy_ram of this ShowEvaluationProjectDetailResponse.
        :rtype: str
        """
        return self._source_db_phy_ram

    @source_db_phy_ram.setter
    def source_db_phy_ram(self, source_db_phy_ram):
        """Sets the source_db_phy_ram of this ShowEvaluationProjectDetailResponse.

        数据库物理RAM。

        :param source_db_phy_ram: The source_db_phy_ram of this ShowEvaluationProjectDetailResponse.
        :type source_db_phy_ram: str
        """
        self._source_db_phy_ram = source_db_phy_ram

    @property
    def source_db_version(self):
        """Gets the source_db_version of this ShowEvaluationProjectDetailResponse.

        数据库版本。

        :return: The source_db_version of this ShowEvaluationProjectDetailResponse.
        :rtype: str
        """
        return self._source_db_version

    @source_db_version.setter
    def source_db_version(self, source_db_version):
        """Sets the source_db_version of this ShowEvaluationProjectDetailResponse.

        数据库版本。

        :param source_db_version: The source_db_version of this ShowEvaluationProjectDetailResponse.
        :type source_db_version: str
        """
        self._source_db_version = source_db_version

    @property
    def source_db_conf(self):
        """Gets the source_db_conf of this ShowEvaluationProjectDetailResponse.

        数据库配置。

        :return: The source_db_conf of this ShowEvaluationProjectDetailResponse.
        :rtype: str
        """
        return self._source_db_conf

    @source_db_conf.setter
    def source_db_conf(self, source_db_conf):
        """Sets the source_db_conf of this ShowEvaluationProjectDetailResponse.

        数据库配置。

        :param source_db_conf: The source_db_conf of this ShowEvaluationProjectDetailResponse.
        :type source_db_conf: str
        """
        self._source_db_conf = source_db_conf

    @property
    def source_db_clock(self):
        """Gets the source_db_clock of this ShowEvaluationProjectDetailResponse.

        数据库时区。

        :return: The source_db_clock of this ShowEvaluationProjectDetailResponse.
        :rtype: str
        """
        return self._source_db_clock

    @source_db_clock.setter
    def source_db_clock(self, source_db_clock):
        """Sets the source_db_clock of this ShowEvaluationProjectDetailResponse.

        数据库时区。

        :param source_db_clock: The source_db_clock of this ShowEvaluationProjectDetailResponse.
        :type source_db_clock: str
        """
        self._source_db_clock = source_db_clock

    @property
    def evaluation_project_id(self):
        """Gets the evaluation_project_id of this ShowEvaluationProjectDetailResponse.

        评估项目ID。

        :return: The evaluation_project_id of this ShowEvaluationProjectDetailResponse.
        :rtype: int
        """
        return self._evaluation_project_id

    @evaluation_project_id.setter
    def evaluation_project_id(self, evaluation_project_id):
        """Sets the evaluation_project_id of this ShowEvaluationProjectDetailResponse.

        评估项目ID。

        :param evaluation_project_id: The evaluation_project_id of this ShowEvaluationProjectDetailResponse.
        :type evaluation_project_id: int
        """
        self._evaluation_project_id = evaluation_project_id

    @property
    def evaluation_project_name(self):
        """Gets the evaluation_project_name of this ShowEvaluationProjectDetailResponse.

        评估项目名称。

        :return: The evaluation_project_name of this ShowEvaluationProjectDetailResponse.
        :rtype: str
        """
        return self._evaluation_project_name

    @evaluation_project_name.setter
    def evaluation_project_name(self, evaluation_project_name):
        """Sets the evaluation_project_name of this ShowEvaluationProjectDetailResponse.

        评估项目名称。

        :param evaluation_project_name: The evaluation_project_name of this ShowEvaluationProjectDetailResponse.
        :type evaluation_project_name: str
        """
        self._evaluation_project_name = evaluation_project_name

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
        if not isinstance(other, ShowEvaluationProjectDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
