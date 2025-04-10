# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultiTaskInitBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ext_info': 'MultiTaskInitBodyExtInfo',
        'source_datasource_id': 'str',
        'target_datasource_id': 'str',
        'task_id': 'str',
        'auto_mapping': 'bool'
    }

    attribute_map = {
        'ext_info': 'ext_info',
        'source_datasource_id': 'source_datasource_id',
        'target_datasource_id': 'target_datasource_id',
        'task_id': 'task_id',
        'auto_mapping': 'auto_mapping'
    }

    def __init__(self, ext_info=None, source_datasource_id=None, target_datasource_id=None, task_id=None, auto_mapping=None):
        r"""MultiTaskInitBody

        The model defined in huaweicloud sdk

        :param ext_info: 
        :type ext_info: :class:`huaweicloudsdkroma.v2.MultiTaskInitBodyExtInfo`
        :param source_datasource_id: 源端数据源ID
        :type source_datasource_id: str
        :param target_datasource_id: 目标端数据源ID
        :type target_datasource_id: str
        :param task_id: 任务ID，可以为空，为空时自动分配任务ID
        :type task_id: str
        :param auto_mapping: 是否自动建立源端到目标端映射
        :type auto_mapping: bool
        """
        
        

        self._ext_info = None
        self._source_datasource_id = None
        self._target_datasource_id = None
        self._task_id = None
        self._auto_mapping = None
        self.discriminator = None

        if ext_info is not None:
            self.ext_info = ext_info
        if source_datasource_id is not None:
            self.source_datasource_id = source_datasource_id
        if target_datasource_id is not None:
            self.target_datasource_id = target_datasource_id
        if task_id is not None:
            self.task_id = task_id
        if auto_mapping is not None:
            self.auto_mapping = auto_mapping

    @property
    def ext_info(self):
        r"""Gets the ext_info of this MultiTaskInitBody.

        :return: The ext_info of this MultiTaskInitBody.
        :rtype: :class:`huaweicloudsdkroma.v2.MultiTaskInitBodyExtInfo`
        """
        return self._ext_info

    @ext_info.setter
    def ext_info(self, ext_info):
        r"""Sets the ext_info of this MultiTaskInitBody.

        :param ext_info: The ext_info of this MultiTaskInitBody.
        :type ext_info: :class:`huaweicloudsdkroma.v2.MultiTaskInitBodyExtInfo`
        """
        self._ext_info = ext_info

    @property
    def source_datasource_id(self):
        r"""Gets the source_datasource_id of this MultiTaskInitBody.

        源端数据源ID

        :return: The source_datasource_id of this MultiTaskInitBody.
        :rtype: str
        """
        return self._source_datasource_id

    @source_datasource_id.setter
    def source_datasource_id(self, source_datasource_id):
        r"""Sets the source_datasource_id of this MultiTaskInitBody.

        源端数据源ID

        :param source_datasource_id: The source_datasource_id of this MultiTaskInitBody.
        :type source_datasource_id: str
        """
        self._source_datasource_id = source_datasource_id

    @property
    def target_datasource_id(self):
        r"""Gets the target_datasource_id of this MultiTaskInitBody.

        目标端数据源ID

        :return: The target_datasource_id of this MultiTaskInitBody.
        :rtype: str
        """
        return self._target_datasource_id

    @target_datasource_id.setter
    def target_datasource_id(self, target_datasource_id):
        r"""Sets the target_datasource_id of this MultiTaskInitBody.

        目标端数据源ID

        :param target_datasource_id: The target_datasource_id of this MultiTaskInitBody.
        :type target_datasource_id: str
        """
        self._target_datasource_id = target_datasource_id

    @property
    def task_id(self):
        r"""Gets the task_id of this MultiTaskInitBody.

        任务ID，可以为空，为空时自动分配任务ID

        :return: The task_id of this MultiTaskInitBody.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this MultiTaskInitBody.

        任务ID，可以为空，为空时自动分配任务ID

        :param task_id: The task_id of this MultiTaskInitBody.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def auto_mapping(self):
        r"""Gets the auto_mapping of this MultiTaskInitBody.

        是否自动建立源端到目标端映射

        :return: The auto_mapping of this MultiTaskInitBody.
        :rtype: bool
        """
        return self._auto_mapping

    @auto_mapping.setter
    def auto_mapping(self, auto_mapping):
        r"""Sets the auto_mapping of this MultiTaskInitBody.

        是否自动建立源端到目标端映射

        :param auto_mapping: The auto_mapping of this MultiTaskInitBody.
        :type auto_mapping: bool
        """
        self._auto_mapping = auto_mapping

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
        if not isinstance(other, MultiTaskInitBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
