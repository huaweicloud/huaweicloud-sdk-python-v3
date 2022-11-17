# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEvaluationProjectReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evaluation_project_name': 'str',
        'source_db_info': 'SourceDBInfo',
        'schemas_info': 'SchemaInfo',
        'objects_type_info': 'ObjectTypeInfo'
    }

    attribute_map = {
        'evaluation_project_name': 'evaluation_project_name',
        'source_db_info': 'source_db_info',
        'schemas_info': 'schemas_info',
        'objects_type_info': 'objects_type_info'
    }

    def __init__(self, evaluation_project_name=None, source_db_info=None, schemas_info=None, objects_type_info=None):
        """CreateEvaluationProjectReq

        The model defined in huaweicloud sdk

        :param evaluation_project_name: 评估项目名称。长度为5-50个字符，以英文字母开头，英文字母或数字结束，允许包含下划线和中划线。不允许重复。
        :type evaluation_project_name: str
        :param source_db_info: 
        :type source_db_info: :class:`huaweicloudsdkugo.v1.SourceDBInfo`
        :param schemas_info: 
        :type schemas_info: :class:`huaweicloudsdkugo.v1.SchemaInfo`
        :param objects_type_info: 
        :type objects_type_info: :class:`huaweicloudsdkugo.v1.ObjectTypeInfo`
        """
        
        

        self._evaluation_project_name = None
        self._source_db_info = None
        self._schemas_info = None
        self._objects_type_info = None
        self.discriminator = None

        self.evaluation_project_name = evaluation_project_name
        self.source_db_info = source_db_info
        self.schemas_info = schemas_info
        self.objects_type_info = objects_type_info

    @property
    def evaluation_project_name(self):
        """Gets the evaluation_project_name of this CreateEvaluationProjectReq.

        评估项目名称。长度为5-50个字符，以英文字母开头，英文字母或数字结束，允许包含下划线和中划线。不允许重复。

        :return: The evaluation_project_name of this CreateEvaluationProjectReq.
        :rtype: str
        """
        return self._evaluation_project_name

    @evaluation_project_name.setter
    def evaluation_project_name(self, evaluation_project_name):
        """Sets the evaluation_project_name of this CreateEvaluationProjectReq.

        评估项目名称。长度为5-50个字符，以英文字母开头，英文字母或数字结束，允许包含下划线和中划线。不允许重复。

        :param evaluation_project_name: The evaluation_project_name of this CreateEvaluationProjectReq.
        :type evaluation_project_name: str
        """
        self._evaluation_project_name = evaluation_project_name

    @property
    def source_db_info(self):
        """Gets the source_db_info of this CreateEvaluationProjectReq.

        :return: The source_db_info of this CreateEvaluationProjectReq.
        :rtype: :class:`huaweicloudsdkugo.v1.SourceDBInfo`
        """
        return self._source_db_info

    @source_db_info.setter
    def source_db_info(self, source_db_info):
        """Sets the source_db_info of this CreateEvaluationProjectReq.

        :param source_db_info: The source_db_info of this CreateEvaluationProjectReq.
        :type source_db_info: :class:`huaweicloudsdkugo.v1.SourceDBInfo`
        """
        self._source_db_info = source_db_info

    @property
    def schemas_info(self):
        """Gets the schemas_info of this CreateEvaluationProjectReq.

        :return: The schemas_info of this CreateEvaluationProjectReq.
        :rtype: :class:`huaweicloudsdkugo.v1.SchemaInfo`
        """
        return self._schemas_info

    @schemas_info.setter
    def schemas_info(self, schemas_info):
        """Sets the schemas_info of this CreateEvaluationProjectReq.

        :param schemas_info: The schemas_info of this CreateEvaluationProjectReq.
        :type schemas_info: :class:`huaweicloudsdkugo.v1.SchemaInfo`
        """
        self._schemas_info = schemas_info

    @property
    def objects_type_info(self):
        """Gets the objects_type_info of this CreateEvaluationProjectReq.

        :return: The objects_type_info of this CreateEvaluationProjectReq.
        :rtype: :class:`huaweicloudsdkugo.v1.ObjectTypeInfo`
        """
        return self._objects_type_info

    @objects_type_info.setter
    def objects_type_info(self, objects_type_info):
        """Sets the objects_type_info of this CreateEvaluationProjectReq.

        :param objects_type_info: The objects_type_info of this CreateEvaluationProjectReq.
        :type objects_type_info: :class:`huaweicloudsdkugo.v1.ObjectTypeInfo`
        """
        self._objects_type_info = objects_type_info

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
        if not isinstance(other, CreateEvaluationProjectReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
