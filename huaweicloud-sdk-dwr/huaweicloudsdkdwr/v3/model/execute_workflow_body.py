# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteWorkflowBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket': 'str',
        'object': 'str',
        'inputs': 'Input'
    }

    attribute_map = {
        'bucket': 'bucket',
        'object': 'object',
        'inputs': 'inputs'
    }

    def __init__(self, bucket=None, object=None, inputs=None):
        """ExecuteWorkflowBody

        The model defined in huaweicloud sdk

        :param bucket: 桶名
        :type bucket: str
        :param object: 对象名
        :type object: str
        :param inputs: 
        :type inputs: :class:`huaweicloudsdkdwr.v3.Input`
        """
        
        

        self._bucket = None
        self._object = None
        self._inputs = None
        self.discriminator = None

        self.bucket = bucket
        self.object = object
        if inputs is not None:
            self.inputs = inputs

    @property
    def bucket(self):
        """Gets the bucket of this ExecuteWorkflowBody.

        桶名

        :return: The bucket of this ExecuteWorkflowBody.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this ExecuteWorkflowBody.

        桶名

        :param bucket: The bucket of this ExecuteWorkflowBody.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def object(self):
        """Gets the object of this ExecuteWorkflowBody.

        对象名

        :return: The object of this ExecuteWorkflowBody.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this ExecuteWorkflowBody.

        对象名

        :param object: The object of this ExecuteWorkflowBody.
        :type object: str
        """
        self._object = object

    @property
    def inputs(self):
        """Gets the inputs of this ExecuteWorkflowBody.

        :return: The inputs of this ExecuteWorkflowBody.
        :rtype: :class:`huaweicloudsdkdwr.v3.Input`
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this ExecuteWorkflowBody.

        :param inputs: The inputs of this ExecuteWorkflowBody.
        :type inputs: :class:`huaweicloudsdkdwr.v3.Input`
        """
        self._inputs = inputs

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
        if not isinstance(other, ExecuteWorkflowBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
