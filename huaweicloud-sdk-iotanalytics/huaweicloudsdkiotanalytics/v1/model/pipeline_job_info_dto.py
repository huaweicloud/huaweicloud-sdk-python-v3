# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineJobInfoDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pipeline_id': 'str',
        'pipeline_name': 'str',
        'data_source_id': 'str',
        'data_store_list': 'list[DataStoreDto]',
        'pipeline_description': 'str',
        'tag_list': 'list[TagInfoDto]',
        'pipeline_state': 'str',
        'status': 'str',
        'rtu': 'int',
        'created_time': 'str',
        'modified_time': 'str',
        'user_id': 'str',
        'has_savepoint': 'bool'
    }

    attribute_map = {
        'pipeline_id': 'pipeline_id',
        'pipeline_name': 'pipeline_name',
        'data_source_id': 'data_source_id',
        'data_store_list': 'data_store_list',
        'pipeline_description': 'pipeline_description',
        'tag_list': 'tag_list',
        'pipeline_state': 'pipeline_state',
        'status': 'status',
        'rtu': 'rtu',
        'created_time': 'created_time',
        'modified_time': 'modified_time',
        'user_id': 'user_id',
        'has_savepoint': 'has_savepoint'
    }

    def __init__(self, pipeline_id=None, pipeline_name=None, data_source_id=None, data_store_list=None, pipeline_description=None, tag_list=None, pipeline_state=None, status=None, rtu=None, created_time=None, modified_time=None, user_id=None, has_savepoint=None):
        """PipelineJobInfoDto

        The model defined in huaweicloud sdk

        :param pipeline_id: 管道ID
        :type pipeline_id: str
        :param pipeline_name: 管道名称
        :type pipeline_name: str
        :param data_source_id: 数据源ID
        :type data_source_id: str
        :param data_store_list: 存储列表
        :type data_store_list: list[:class:`huaweicloudsdkiotanalytics.v1.DataStoreDto`]
        :param pipeline_description: 管道描述
        :type pipeline_description: str
        :param tag_list: 存储列表
        :type tag_list: list[:class:`huaweicloudsdkiotanalytics.v1.TagInfoDto`]
        :param pipeline_state: 管道状态
        :type pipeline_state: str
        :param status: 操作状态
        :type status: str
        :param rtu: 运行管道的RTU个数
        :type rtu: int
        :param created_time: 创建时间
        :type created_time: str
        :param modified_time: 修改时间
        :type modified_time: str
        :param user_id: 用户ID
        :type user_id: str
        :param has_savepoint: 已停止的管道作业是否有历史缓存数据
        :type has_savepoint: bool
        """
        
        

        self._pipeline_id = None
        self._pipeline_name = None
        self._data_source_id = None
        self._data_store_list = None
        self._pipeline_description = None
        self._tag_list = None
        self._pipeline_state = None
        self._status = None
        self._rtu = None
        self._created_time = None
        self._modified_time = None
        self._user_id = None
        self._has_savepoint = None
        self.discriminator = None

        if pipeline_id is not None:
            self.pipeline_id = pipeline_id
        if pipeline_name is not None:
            self.pipeline_name = pipeline_name
        if data_source_id is not None:
            self.data_source_id = data_source_id
        if data_store_list is not None:
            self.data_store_list = data_store_list
        if pipeline_description is not None:
            self.pipeline_description = pipeline_description
        if tag_list is not None:
            self.tag_list = tag_list
        if pipeline_state is not None:
            self.pipeline_state = pipeline_state
        if status is not None:
            self.status = status
        if rtu is not None:
            self.rtu = rtu
        if created_time is not None:
            self.created_time = created_time
        if modified_time is not None:
            self.modified_time = modified_time
        if user_id is not None:
            self.user_id = user_id
        if has_savepoint is not None:
            self.has_savepoint = has_savepoint

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this PipelineJobInfoDto.

        管道ID

        :return: The pipeline_id of this PipelineJobInfoDto.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this PipelineJobInfoDto.

        管道ID

        :param pipeline_id: The pipeline_id of this PipelineJobInfoDto.
        :type pipeline_id: str
        """
        self._pipeline_id = pipeline_id

    @property
    def pipeline_name(self):
        """Gets the pipeline_name of this PipelineJobInfoDto.

        管道名称

        :return: The pipeline_name of this PipelineJobInfoDto.
        :rtype: str
        """
        return self._pipeline_name

    @pipeline_name.setter
    def pipeline_name(self, pipeline_name):
        """Sets the pipeline_name of this PipelineJobInfoDto.

        管道名称

        :param pipeline_name: The pipeline_name of this PipelineJobInfoDto.
        :type pipeline_name: str
        """
        self._pipeline_name = pipeline_name

    @property
    def data_source_id(self):
        """Gets the data_source_id of this PipelineJobInfoDto.

        数据源ID

        :return: The data_source_id of this PipelineJobInfoDto.
        :rtype: str
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        """Sets the data_source_id of this PipelineJobInfoDto.

        数据源ID

        :param data_source_id: The data_source_id of this PipelineJobInfoDto.
        :type data_source_id: str
        """
        self._data_source_id = data_source_id

    @property
    def data_store_list(self):
        """Gets the data_store_list of this PipelineJobInfoDto.

        存储列表

        :return: The data_store_list of this PipelineJobInfoDto.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.DataStoreDto`]
        """
        return self._data_store_list

    @data_store_list.setter
    def data_store_list(self, data_store_list):
        """Sets the data_store_list of this PipelineJobInfoDto.

        存储列表

        :param data_store_list: The data_store_list of this PipelineJobInfoDto.
        :type data_store_list: list[:class:`huaweicloudsdkiotanalytics.v1.DataStoreDto`]
        """
        self._data_store_list = data_store_list

    @property
    def pipeline_description(self):
        """Gets the pipeline_description of this PipelineJobInfoDto.

        管道描述

        :return: The pipeline_description of this PipelineJobInfoDto.
        :rtype: str
        """
        return self._pipeline_description

    @pipeline_description.setter
    def pipeline_description(self, pipeline_description):
        """Sets the pipeline_description of this PipelineJobInfoDto.

        管道描述

        :param pipeline_description: The pipeline_description of this PipelineJobInfoDto.
        :type pipeline_description: str
        """
        self._pipeline_description = pipeline_description

    @property
    def tag_list(self):
        """Gets the tag_list of this PipelineJobInfoDto.

        存储列表

        :return: The tag_list of this PipelineJobInfoDto.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.TagInfoDto`]
        """
        return self._tag_list

    @tag_list.setter
    def tag_list(self, tag_list):
        """Sets the tag_list of this PipelineJobInfoDto.

        存储列表

        :param tag_list: The tag_list of this PipelineJobInfoDto.
        :type tag_list: list[:class:`huaweicloudsdkiotanalytics.v1.TagInfoDto`]
        """
        self._tag_list = tag_list

    @property
    def pipeline_state(self):
        """Gets the pipeline_state of this PipelineJobInfoDto.

        管道状态

        :return: The pipeline_state of this PipelineJobInfoDto.
        :rtype: str
        """
        return self._pipeline_state

    @pipeline_state.setter
    def pipeline_state(self, pipeline_state):
        """Sets the pipeline_state of this PipelineJobInfoDto.

        管道状态

        :param pipeline_state: The pipeline_state of this PipelineJobInfoDto.
        :type pipeline_state: str
        """
        self._pipeline_state = pipeline_state

    @property
    def status(self):
        """Gets the status of this PipelineJobInfoDto.

        操作状态

        :return: The status of this PipelineJobInfoDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PipelineJobInfoDto.

        操作状态

        :param status: The status of this PipelineJobInfoDto.
        :type status: str
        """
        self._status = status

    @property
    def rtu(self):
        """Gets the rtu of this PipelineJobInfoDto.

        运行管道的RTU个数

        :return: The rtu of this PipelineJobInfoDto.
        :rtype: int
        """
        return self._rtu

    @rtu.setter
    def rtu(self, rtu):
        """Sets the rtu of this PipelineJobInfoDto.

        运行管道的RTU个数

        :param rtu: The rtu of this PipelineJobInfoDto.
        :type rtu: int
        """
        self._rtu = rtu

    @property
    def created_time(self):
        """Gets the created_time of this PipelineJobInfoDto.

        创建时间

        :return: The created_time of this PipelineJobInfoDto.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this PipelineJobInfoDto.

        创建时间

        :param created_time: The created_time of this PipelineJobInfoDto.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def modified_time(self):
        """Gets the modified_time of this PipelineJobInfoDto.

        修改时间

        :return: The modified_time of this PipelineJobInfoDto.
        :rtype: str
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        """Sets the modified_time of this PipelineJobInfoDto.

        修改时间

        :param modified_time: The modified_time of this PipelineJobInfoDto.
        :type modified_time: str
        """
        self._modified_time = modified_time

    @property
    def user_id(self):
        """Gets the user_id of this PipelineJobInfoDto.

        用户ID

        :return: The user_id of this PipelineJobInfoDto.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this PipelineJobInfoDto.

        用户ID

        :param user_id: The user_id of this PipelineJobInfoDto.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def has_savepoint(self):
        """Gets the has_savepoint of this PipelineJobInfoDto.

        已停止的管道作业是否有历史缓存数据

        :return: The has_savepoint of this PipelineJobInfoDto.
        :rtype: bool
        """
        return self._has_savepoint

    @has_savepoint.setter
    def has_savepoint(self, has_savepoint):
        """Sets the has_savepoint of this PipelineJobInfoDto.

        已停止的管道作业是否有历史缓存数据

        :param has_savepoint: The has_savepoint of this PipelineJobInfoDto.
        :type has_savepoint: bool
        """
        self._has_savepoint = has_savepoint

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
        if not isinstance(other, PipelineJobInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
