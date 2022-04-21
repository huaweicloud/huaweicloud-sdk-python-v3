# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultiTaskInitElement:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ext_info': 'MultiTaskInitElementExtInfo',
        'task_id': 'str',
        'source_datasource_id': 'str',
        'target_datasource_id': 'str',
        'source_group': 'str',
        'target_group': 'str',
        'source_ds_id': 'str',
        'target_ds_id': 'str',
        'source_instance_id': 'str',
        'target_instance_id': 'str',
        'source_app_id': 'str',
        'target_app_id': 'str',
        'source_datasource_name': 'str',
        'target_datasource_name': 'str',
        'source_datasource_type': 'str',
        'target_datasource_type': 'str',
        'mappings': 'list[MultiTaskMappingElement]',
        'mappings_total_count': 'int'
    }

    attribute_map = {
        'ext_info': 'ext_info',
        'task_id': 'task_id',
        'source_datasource_id': 'source_datasource_id',
        'target_datasource_id': 'target_datasource_id',
        'source_group': 'source_group',
        'target_group': 'target_group',
        'source_ds_id': 'source_ds_id',
        'target_ds_id': 'target_ds_id',
        'source_instance_id': 'source_instance_id',
        'target_instance_id': 'target_instance_id',
        'source_app_id': 'source_app_id',
        'target_app_id': 'target_app_id',
        'source_datasource_name': 'source_datasource_name',
        'target_datasource_name': 'target_datasource_name',
        'source_datasource_type': 'source_datasource_type',
        'target_datasource_type': 'target_datasource_type',
        'mappings': 'mappings',
        'mappings_total_count': 'mappings_total_count'
    }

    def __init__(self, ext_info=None, task_id=None, source_datasource_id=None, target_datasource_id=None, source_group=None, target_group=None, source_ds_id=None, target_ds_id=None, source_instance_id=None, target_instance_id=None, source_app_id=None, target_app_id=None, source_datasource_name=None, target_datasource_name=None, source_datasource_type=None, target_datasource_type=None, mappings=None, mappings_total_count=None):
        """MultiTaskInitElement

        The model defined in huaweicloud sdk

        :param ext_info: 
        :type ext_info: :class:`huaweicloudsdkroma.v2.MultiTaskInitElementExtInfo`
        :param task_id: 任务ID
        :type task_id: str
        :param source_datasource_id: 源端数据源ID
        :type source_datasource_id: str
        :param target_datasource_id: 目标端数据源ID
        :type target_datasource_id: str
        :param source_group: 源端组
        :type source_group: str
        :param target_group: 目标端组
        :type target_group: str
        :param source_ds_id: 源端数据源ID
        :type source_ds_id: str
        :param target_ds_id: 目标端数据源ID
        :type target_ds_id: str
        :param source_instance_id: 源端实例ID
        :type source_instance_id: str
        :param target_instance_id: 目标端实例ID
        :type target_instance_id: str
        :param source_app_id: 源端数据源所属集成应用ID
        :type source_app_id: str
        :param target_app_id: 目标端数据源所属集成应用ID
        :type target_app_id: str
        :param source_datasource_name: 源端数据源的名称
        :type source_datasource_name: str
        :param target_datasource_name: 目标端数据源的名称
        :type target_datasource_name: str
        :param source_datasource_type: 源端数据源的类型
        :type source_datasource_type: str
        :param target_datasource_type: 目标端数据源的类型
        :type target_datasource_type: str
        :param mappings: 映射关系列表，只返回前10条
        :type mappings: list[:class:`huaweicloudsdkroma.v2.MultiTaskMappingElement`]
        :param mappings_total_count: 映射关系总数
        :type mappings_total_count: int
        """
        
        

        self._ext_info = None
        self._task_id = None
        self._source_datasource_id = None
        self._target_datasource_id = None
        self._source_group = None
        self._target_group = None
        self._source_ds_id = None
        self._target_ds_id = None
        self._source_instance_id = None
        self._target_instance_id = None
        self._source_app_id = None
        self._target_app_id = None
        self._source_datasource_name = None
        self._target_datasource_name = None
        self._source_datasource_type = None
        self._target_datasource_type = None
        self._mappings = None
        self._mappings_total_count = None
        self.discriminator = None

        if ext_info is not None:
            self.ext_info = ext_info
        if task_id is not None:
            self.task_id = task_id
        if source_datasource_id is not None:
            self.source_datasource_id = source_datasource_id
        if target_datasource_id is not None:
            self.target_datasource_id = target_datasource_id
        if source_group is not None:
            self.source_group = source_group
        if target_group is not None:
            self.target_group = target_group
        if source_ds_id is not None:
            self.source_ds_id = source_ds_id
        if target_ds_id is not None:
            self.target_ds_id = target_ds_id
        if source_instance_id is not None:
            self.source_instance_id = source_instance_id
        if target_instance_id is not None:
            self.target_instance_id = target_instance_id
        if source_app_id is not None:
            self.source_app_id = source_app_id
        if target_app_id is not None:
            self.target_app_id = target_app_id
        if source_datasource_name is not None:
            self.source_datasource_name = source_datasource_name
        if target_datasource_name is not None:
            self.target_datasource_name = target_datasource_name
        if source_datasource_type is not None:
            self.source_datasource_type = source_datasource_type
        if target_datasource_type is not None:
            self.target_datasource_type = target_datasource_type
        if mappings is not None:
            self.mappings = mappings
        if mappings_total_count is not None:
            self.mappings_total_count = mappings_total_count

    @property
    def ext_info(self):
        """Gets the ext_info of this MultiTaskInitElement.


        :return: The ext_info of this MultiTaskInitElement.
        :rtype: :class:`huaweicloudsdkroma.v2.MultiTaskInitElementExtInfo`
        """
        return self._ext_info

    @ext_info.setter
    def ext_info(self, ext_info):
        """Sets the ext_info of this MultiTaskInitElement.


        :param ext_info: The ext_info of this MultiTaskInitElement.
        :type ext_info: :class:`huaweicloudsdkroma.v2.MultiTaskInitElementExtInfo`
        """
        self._ext_info = ext_info

    @property
    def task_id(self):
        """Gets the task_id of this MultiTaskInitElement.

        任务ID

        :return: The task_id of this MultiTaskInitElement.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this MultiTaskInitElement.

        任务ID

        :param task_id: The task_id of this MultiTaskInitElement.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def source_datasource_id(self):
        """Gets the source_datasource_id of this MultiTaskInitElement.

        源端数据源ID

        :return: The source_datasource_id of this MultiTaskInitElement.
        :rtype: str
        """
        return self._source_datasource_id

    @source_datasource_id.setter
    def source_datasource_id(self, source_datasource_id):
        """Sets the source_datasource_id of this MultiTaskInitElement.

        源端数据源ID

        :param source_datasource_id: The source_datasource_id of this MultiTaskInitElement.
        :type source_datasource_id: str
        """
        self._source_datasource_id = source_datasource_id

    @property
    def target_datasource_id(self):
        """Gets the target_datasource_id of this MultiTaskInitElement.

        目标端数据源ID

        :return: The target_datasource_id of this MultiTaskInitElement.
        :rtype: str
        """
        return self._target_datasource_id

    @target_datasource_id.setter
    def target_datasource_id(self, target_datasource_id):
        """Sets the target_datasource_id of this MultiTaskInitElement.

        目标端数据源ID

        :param target_datasource_id: The target_datasource_id of this MultiTaskInitElement.
        :type target_datasource_id: str
        """
        self._target_datasource_id = target_datasource_id

    @property
    def source_group(self):
        """Gets the source_group of this MultiTaskInitElement.

        源端组

        :return: The source_group of this MultiTaskInitElement.
        :rtype: str
        """
        return self._source_group

    @source_group.setter
    def source_group(self, source_group):
        """Sets the source_group of this MultiTaskInitElement.

        源端组

        :param source_group: The source_group of this MultiTaskInitElement.
        :type source_group: str
        """
        self._source_group = source_group

    @property
    def target_group(self):
        """Gets the target_group of this MultiTaskInitElement.

        目标端组

        :return: The target_group of this MultiTaskInitElement.
        :rtype: str
        """
        return self._target_group

    @target_group.setter
    def target_group(self, target_group):
        """Sets the target_group of this MultiTaskInitElement.

        目标端组

        :param target_group: The target_group of this MultiTaskInitElement.
        :type target_group: str
        """
        self._target_group = target_group

    @property
    def source_ds_id(self):
        """Gets the source_ds_id of this MultiTaskInitElement.

        源端数据源ID

        :return: The source_ds_id of this MultiTaskInitElement.
        :rtype: str
        """
        return self._source_ds_id

    @source_ds_id.setter
    def source_ds_id(self, source_ds_id):
        """Sets the source_ds_id of this MultiTaskInitElement.

        源端数据源ID

        :param source_ds_id: The source_ds_id of this MultiTaskInitElement.
        :type source_ds_id: str
        """
        self._source_ds_id = source_ds_id

    @property
    def target_ds_id(self):
        """Gets the target_ds_id of this MultiTaskInitElement.

        目标端数据源ID

        :return: The target_ds_id of this MultiTaskInitElement.
        :rtype: str
        """
        return self._target_ds_id

    @target_ds_id.setter
    def target_ds_id(self, target_ds_id):
        """Sets the target_ds_id of this MultiTaskInitElement.

        目标端数据源ID

        :param target_ds_id: The target_ds_id of this MultiTaskInitElement.
        :type target_ds_id: str
        """
        self._target_ds_id = target_ds_id

    @property
    def source_instance_id(self):
        """Gets the source_instance_id of this MultiTaskInitElement.

        源端实例ID

        :return: The source_instance_id of this MultiTaskInitElement.
        :rtype: str
        """
        return self._source_instance_id

    @source_instance_id.setter
    def source_instance_id(self, source_instance_id):
        """Sets the source_instance_id of this MultiTaskInitElement.

        源端实例ID

        :param source_instance_id: The source_instance_id of this MultiTaskInitElement.
        :type source_instance_id: str
        """
        self._source_instance_id = source_instance_id

    @property
    def target_instance_id(self):
        """Gets the target_instance_id of this MultiTaskInitElement.

        目标端实例ID

        :return: The target_instance_id of this MultiTaskInitElement.
        :rtype: str
        """
        return self._target_instance_id

    @target_instance_id.setter
    def target_instance_id(self, target_instance_id):
        """Sets the target_instance_id of this MultiTaskInitElement.

        目标端实例ID

        :param target_instance_id: The target_instance_id of this MultiTaskInitElement.
        :type target_instance_id: str
        """
        self._target_instance_id = target_instance_id

    @property
    def source_app_id(self):
        """Gets the source_app_id of this MultiTaskInitElement.

        源端数据源所属集成应用ID

        :return: The source_app_id of this MultiTaskInitElement.
        :rtype: str
        """
        return self._source_app_id

    @source_app_id.setter
    def source_app_id(self, source_app_id):
        """Sets the source_app_id of this MultiTaskInitElement.

        源端数据源所属集成应用ID

        :param source_app_id: The source_app_id of this MultiTaskInitElement.
        :type source_app_id: str
        """
        self._source_app_id = source_app_id

    @property
    def target_app_id(self):
        """Gets the target_app_id of this MultiTaskInitElement.

        目标端数据源所属集成应用ID

        :return: The target_app_id of this MultiTaskInitElement.
        :rtype: str
        """
        return self._target_app_id

    @target_app_id.setter
    def target_app_id(self, target_app_id):
        """Sets the target_app_id of this MultiTaskInitElement.

        目标端数据源所属集成应用ID

        :param target_app_id: The target_app_id of this MultiTaskInitElement.
        :type target_app_id: str
        """
        self._target_app_id = target_app_id

    @property
    def source_datasource_name(self):
        """Gets the source_datasource_name of this MultiTaskInitElement.

        源端数据源的名称

        :return: The source_datasource_name of this MultiTaskInitElement.
        :rtype: str
        """
        return self._source_datasource_name

    @source_datasource_name.setter
    def source_datasource_name(self, source_datasource_name):
        """Sets the source_datasource_name of this MultiTaskInitElement.

        源端数据源的名称

        :param source_datasource_name: The source_datasource_name of this MultiTaskInitElement.
        :type source_datasource_name: str
        """
        self._source_datasource_name = source_datasource_name

    @property
    def target_datasource_name(self):
        """Gets the target_datasource_name of this MultiTaskInitElement.

        目标端数据源的名称

        :return: The target_datasource_name of this MultiTaskInitElement.
        :rtype: str
        """
        return self._target_datasource_name

    @target_datasource_name.setter
    def target_datasource_name(self, target_datasource_name):
        """Sets the target_datasource_name of this MultiTaskInitElement.

        目标端数据源的名称

        :param target_datasource_name: The target_datasource_name of this MultiTaskInitElement.
        :type target_datasource_name: str
        """
        self._target_datasource_name = target_datasource_name

    @property
    def source_datasource_type(self):
        """Gets the source_datasource_type of this MultiTaskInitElement.

        源端数据源的类型

        :return: The source_datasource_type of this MultiTaskInitElement.
        :rtype: str
        """
        return self._source_datasource_type

    @source_datasource_type.setter
    def source_datasource_type(self, source_datasource_type):
        """Sets the source_datasource_type of this MultiTaskInitElement.

        源端数据源的类型

        :param source_datasource_type: The source_datasource_type of this MultiTaskInitElement.
        :type source_datasource_type: str
        """
        self._source_datasource_type = source_datasource_type

    @property
    def target_datasource_type(self):
        """Gets the target_datasource_type of this MultiTaskInitElement.

        目标端数据源的类型

        :return: The target_datasource_type of this MultiTaskInitElement.
        :rtype: str
        """
        return self._target_datasource_type

    @target_datasource_type.setter
    def target_datasource_type(self, target_datasource_type):
        """Sets the target_datasource_type of this MultiTaskInitElement.

        目标端数据源的类型

        :param target_datasource_type: The target_datasource_type of this MultiTaskInitElement.
        :type target_datasource_type: str
        """
        self._target_datasource_type = target_datasource_type

    @property
    def mappings(self):
        """Gets the mappings of this MultiTaskInitElement.

        映射关系列表，只返回前10条

        :return: The mappings of this MultiTaskInitElement.
        :rtype: list[:class:`huaweicloudsdkroma.v2.MultiTaskMappingElement`]
        """
        return self._mappings

    @mappings.setter
    def mappings(self, mappings):
        """Sets the mappings of this MultiTaskInitElement.

        映射关系列表，只返回前10条

        :param mappings: The mappings of this MultiTaskInitElement.
        :type mappings: list[:class:`huaweicloudsdkroma.v2.MultiTaskMappingElement`]
        """
        self._mappings = mappings

    @property
    def mappings_total_count(self):
        """Gets the mappings_total_count of this MultiTaskInitElement.

        映射关系总数

        :return: The mappings_total_count of this MultiTaskInitElement.
        :rtype: int
        """
        return self._mappings_total_count

    @mappings_total_count.setter
    def mappings_total_count(self, mappings_total_count):
        """Sets the mappings_total_count of this MultiTaskInitElement.

        映射关系总数

        :param mappings_total_count: The mappings_total_count of this MultiTaskInitElement.
        :type mappings_total_count: int
        """
        self._mappings_total_count = mappings_total_count

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
        if not isinstance(other, MultiTaskInitElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
