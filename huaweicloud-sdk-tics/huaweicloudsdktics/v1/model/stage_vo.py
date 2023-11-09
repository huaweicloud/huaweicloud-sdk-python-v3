# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StageVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'last_step_stage_id': 'list[int]',
        'processors': 'list[ProcessorVo]',
        'stage_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'last_step_stage_id': 'last_step_stage_id',
        'processors': 'processors',
        'stage_name': 'stage_name'
    }

    def __init__(self, id=None, last_step_stage_id=None, processors=None, stage_name=None):
        """StageVo

        The model defined in huaweicloud sdk

        :param id: 执行阶段id
        :type id: int
        :param last_step_stage_id: 上游的stageId
        :type last_step_stage_id: list[int]
        :param processors: 执行过程
        :type processors: list[:class:`huaweicloudsdktics.v1.ProcessorVo`]
        :param stage_name: 执行阶段名称
        :type stage_name: str
        """
        
        

        self._id = None
        self._last_step_stage_id = None
        self._processors = None
        self._stage_name = None
        self.discriminator = None

        self.id = id
        if last_step_stage_id is not None:
            self.last_step_stage_id = last_step_stage_id
        if processors is not None:
            self.processors = processors
        if stage_name is not None:
            self.stage_name = stage_name

    @property
    def id(self):
        """Gets the id of this StageVo.

        执行阶段id

        :return: The id of this StageVo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StageVo.

        执行阶段id

        :param id: The id of this StageVo.
        :type id: int
        """
        self._id = id

    @property
    def last_step_stage_id(self):
        """Gets the last_step_stage_id of this StageVo.

        上游的stageId

        :return: The last_step_stage_id of this StageVo.
        :rtype: list[int]
        """
        return self._last_step_stage_id

    @last_step_stage_id.setter
    def last_step_stage_id(self, last_step_stage_id):
        """Sets the last_step_stage_id of this StageVo.

        上游的stageId

        :param last_step_stage_id: The last_step_stage_id of this StageVo.
        :type last_step_stage_id: list[int]
        """
        self._last_step_stage_id = last_step_stage_id

    @property
    def processors(self):
        """Gets the processors of this StageVo.

        执行过程

        :return: The processors of this StageVo.
        :rtype: list[:class:`huaweicloudsdktics.v1.ProcessorVo`]
        """
        return self._processors

    @processors.setter
    def processors(self, processors):
        """Sets the processors of this StageVo.

        执行过程

        :param processors: The processors of this StageVo.
        :type processors: list[:class:`huaweicloudsdktics.v1.ProcessorVo`]
        """
        self._processors = processors

    @property
    def stage_name(self):
        """Gets the stage_name of this StageVo.

        执行阶段名称

        :return: The stage_name of this StageVo.
        :rtype: str
        """
        return self._stage_name

    @stage_name.setter
    def stage_name(self, stage_name):
        """Sets the stage_name of this StageVo.

        执行阶段名称

        :param stage_name: The stage_name of this StageVo.
        :type stage_name: str
        """
        self._stage_name = stage_name

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
        if not isinstance(other, StageVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
