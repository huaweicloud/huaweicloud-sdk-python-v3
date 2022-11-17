# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoContrast:

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
        'execution_order': 'int',
        'contrast': 'str',
        'brightness': 'str'
    }

    attribute_map = {
        'name': 'name',
        'execution_order': 'execution_order',
        'contrast': 'contrast',
        'brightness': 'brightness'
    }

    def __init__(self, name=None, execution_order=None, contrast=None, brightness=None):
        """VideoContrast

        The model defined in huaweicloud sdk

        :param name: 对比度算法名称\&quot;hw-contrast\&quot;。 
        :type name: str
        :param execution_order: 1 表示视频处理时第一个执行，2表示第二个执行，以此类推；除不执行，各视频处理算法的执行次序不可相同。 
        :type execution_order: int
        :param contrast: 对比度调节的程度， 值越大， 对比度越高。 
        :type contrast: str
        :param brightness: 1 表示视频处理时第一个执行，2表示第二个执行，以此类推；除不执行，各视频处理算法的执行次序不可相同。 
        :type brightness: str
        """
        
        

        self._name = None
        self._execution_order = None
        self._contrast = None
        self._brightness = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if execution_order is not None:
            self.execution_order = execution_order
        if contrast is not None:
            self.contrast = contrast
        if brightness is not None:
            self.brightness = brightness

    @property
    def name(self):
        """Gets the name of this VideoContrast.

        对比度算法名称\"hw-contrast\"。 

        :return: The name of this VideoContrast.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VideoContrast.

        对比度算法名称\"hw-contrast\"。 

        :param name: The name of this VideoContrast.
        :type name: str
        """
        self._name = name

    @property
    def execution_order(self):
        """Gets the execution_order of this VideoContrast.

        1 表示视频处理时第一个执行，2表示第二个执行，以此类推；除不执行，各视频处理算法的执行次序不可相同。 

        :return: The execution_order of this VideoContrast.
        :rtype: int
        """
        return self._execution_order

    @execution_order.setter
    def execution_order(self, execution_order):
        """Sets the execution_order of this VideoContrast.

        1 表示视频处理时第一个执行，2表示第二个执行，以此类推；除不执行，各视频处理算法的执行次序不可相同。 

        :param execution_order: The execution_order of this VideoContrast.
        :type execution_order: int
        """
        self._execution_order = execution_order

    @property
    def contrast(self):
        """Gets the contrast of this VideoContrast.

        对比度调节的程度， 值越大， 对比度越高。 

        :return: The contrast of this VideoContrast.
        :rtype: str
        """
        return self._contrast

    @contrast.setter
    def contrast(self, contrast):
        """Sets the contrast of this VideoContrast.

        对比度调节的程度， 值越大， 对比度越高。 

        :param contrast: The contrast of this VideoContrast.
        :type contrast: str
        """
        self._contrast = contrast

    @property
    def brightness(self):
        """Gets the brightness of this VideoContrast.

        1 表示视频处理时第一个执行，2表示第二个执行，以此类推；除不执行，各视频处理算法的执行次序不可相同。 

        :return: The brightness of this VideoContrast.
        :rtype: str
        """
        return self._brightness

    @brightness.setter
    def brightness(self, brightness):
        """Sets the brightness of this VideoContrast.

        1 表示视频处理时第一个执行，2表示第二个执行，以此类推；除不执行，各视频处理算法的执行次序不可相同。 

        :param brightness: The brightness of this VideoContrast.
        :type brightness: str
        """
        self._brightness = brightness

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
        if not isinstance(other, VideoContrast):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
