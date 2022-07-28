# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckDataTransformationReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'object_info': 'list[DatabaseObjectVO]',
        'transformation_info': 'TransformationInfo',
        'config_transformation': 'ConfigTransformationVo'
    }

    attribute_map = {
        'job_id': 'job_id',
        'object_info': 'object_info',
        'transformation_info': 'transformation_info',
        'config_transformation': 'config_transformation'
    }

    def __init__(self, job_id=None, object_info=None, transformation_info=None, config_transformation=None):
        """CheckDataTransformationReq

        The model defined in huaweicloud sdk

        :param job_id: 任务id
        :type job_id: str
        :param object_info: 对象信息，生成加工规则时需要填写。
        :type object_info: list[:class:`huaweicloudsdkdrs.v3.DatabaseObjectVO`]
        :param transformation_info: 
        :type transformation_info: :class:`huaweicloudsdkdrs.v3.TransformationInfo`
        :param config_transformation: 
        :type config_transformation: :class:`huaweicloudsdkdrs.v3.ConfigTransformationVo`
        """
        
        

        self._job_id = None
        self._object_info = None
        self._transformation_info = None
        self._config_transformation = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if object_info is not None:
            self.object_info = object_info
        self.transformation_info = transformation_info
        if config_transformation is not None:
            self.config_transformation = config_transformation

    @property
    def job_id(self):
        """Gets the job_id of this CheckDataTransformationReq.

        任务id

        :return: The job_id of this CheckDataTransformationReq.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this CheckDataTransformationReq.

        任务id

        :param job_id: The job_id of this CheckDataTransformationReq.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def object_info(self):
        """Gets the object_info of this CheckDataTransformationReq.

        对象信息，生成加工规则时需要填写。

        :return: The object_info of this CheckDataTransformationReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.DatabaseObjectVO`]
        """
        return self._object_info

    @object_info.setter
    def object_info(self, object_info):
        """Sets the object_info of this CheckDataTransformationReq.

        对象信息，生成加工规则时需要填写。

        :param object_info: The object_info of this CheckDataTransformationReq.
        :type object_info: list[:class:`huaweicloudsdkdrs.v3.DatabaseObjectVO`]
        """
        self._object_info = object_info

    @property
    def transformation_info(self):
        """Gets the transformation_info of this CheckDataTransformationReq.


        :return: The transformation_info of this CheckDataTransformationReq.
        :rtype: :class:`huaweicloudsdkdrs.v3.TransformationInfo`
        """
        return self._transformation_info

    @transformation_info.setter
    def transformation_info(self, transformation_info):
        """Sets the transformation_info of this CheckDataTransformationReq.


        :param transformation_info: The transformation_info of this CheckDataTransformationReq.
        :type transformation_info: :class:`huaweicloudsdkdrs.v3.TransformationInfo`
        """
        self._transformation_info = transformation_info

    @property
    def config_transformation(self):
        """Gets the config_transformation of this CheckDataTransformationReq.


        :return: The config_transformation of this CheckDataTransformationReq.
        :rtype: :class:`huaweicloudsdkdrs.v3.ConfigTransformationVo`
        """
        return self._config_transformation

    @config_transformation.setter
    def config_transformation(self, config_transformation):
        """Sets the config_transformation of this CheckDataTransformationReq.


        :param config_transformation: The config_transformation of this CheckDataTransformationReq.
        :type config_transformation: :class:`huaweicloudsdkdrs.v3.ConfigTransformationVo`
        """
        self._config_transformation = config_transformation

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
        if not isinstance(other, CheckDataTransformationReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
