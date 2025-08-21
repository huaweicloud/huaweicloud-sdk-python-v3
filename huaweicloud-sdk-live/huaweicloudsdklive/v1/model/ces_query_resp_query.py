# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CesQueryRespQuery:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'medialive_mpc': 'CesDimsItem',
        'pipeline': 'CesDimsItem',
        'audio': 'CesDimsItem',
        'medialive_cdn': 'CesDimsItem',
        'medialive_package': 'CesDimsItem',
        'medialive_connect': 'CesDimsItem',
        'medialive_tailor': 'CesDimsItem'
    }

    attribute_map = {
        'medialive_mpc': 'medialive_mpc',
        'pipeline': 'pipeline',
        'audio': 'audio',
        'medialive_cdn': 'medialive_cdn',
        'medialive_package': 'medialive_package',
        'medialive_connect': 'medialive_connect',
        'medialive_tailor': 'medialive_tailor'
    }

    def __init__(self, medialive_mpc=None, pipeline=None, audio=None, medialive_cdn=None, medialive_package=None, medialive_connect=None, medialive_tailor=None):
        r"""CesQueryRespQuery

        The model defined in huaweicloud sdk

        :param medialive_mpc: 
        :type medialive_mpc: :class:`huaweicloudsdklive.v1.CesDimsItem`
        :param pipeline: 
        :type pipeline: :class:`huaweicloudsdklive.v1.CesDimsItem`
        :param audio: 
        :type audio: :class:`huaweicloudsdklive.v1.CesDimsItem`
        :param medialive_cdn: 
        :type medialive_cdn: :class:`huaweicloudsdklive.v1.CesDimsItem`
        :param medialive_package: 
        :type medialive_package: :class:`huaweicloudsdklive.v1.CesDimsItem`
        :param medialive_connect: 
        :type medialive_connect: :class:`huaweicloudsdklive.v1.CesDimsItem`
        :param medialive_tailor: 
        :type medialive_tailor: :class:`huaweicloudsdklive.v1.CesDimsItem`
        """
        
        

        self._medialive_mpc = None
        self._pipeline = None
        self._audio = None
        self._medialive_cdn = None
        self._medialive_package = None
        self._medialive_connect = None
        self._medialive_tailor = None
        self.discriminator = None

        self.medialive_mpc = medialive_mpc
        self.pipeline = pipeline
        self.audio = audio
        self.medialive_cdn = medialive_cdn
        self.medialive_package = medialive_package
        self.medialive_connect = medialive_connect
        self.medialive_tailor = medialive_tailor

    @property
    def medialive_mpc(self):
        r"""Gets the medialive_mpc of this CesQueryRespQuery.

        :return: The medialive_mpc of this CesQueryRespQuery.
        :rtype: :class:`huaweicloudsdklive.v1.CesDimsItem`
        """
        return self._medialive_mpc

    @medialive_mpc.setter
    def medialive_mpc(self, medialive_mpc):
        r"""Sets the medialive_mpc of this CesQueryRespQuery.

        :param medialive_mpc: The medialive_mpc of this CesQueryRespQuery.
        :type medialive_mpc: :class:`huaweicloudsdklive.v1.CesDimsItem`
        """
        self._medialive_mpc = medialive_mpc

    @property
    def pipeline(self):
        r"""Gets the pipeline of this CesQueryRespQuery.

        :return: The pipeline of this CesQueryRespQuery.
        :rtype: :class:`huaweicloudsdklive.v1.CesDimsItem`
        """
        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        r"""Sets the pipeline of this CesQueryRespQuery.

        :param pipeline: The pipeline of this CesQueryRespQuery.
        :type pipeline: :class:`huaweicloudsdklive.v1.CesDimsItem`
        """
        self._pipeline = pipeline

    @property
    def audio(self):
        r"""Gets the audio of this CesQueryRespQuery.

        :return: The audio of this CesQueryRespQuery.
        :rtype: :class:`huaweicloudsdklive.v1.CesDimsItem`
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        r"""Sets the audio of this CesQueryRespQuery.

        :param audio: The audio of this CesQueryRespQuery.
        :type audio: :class:`huaweicloudsdklive.v1.CesDimsItem`
        """
        self._audio = audio

    @property
    def medialive_cdn(self):
        r"""Gets the medialive_cdn of this CesQueryRespQuery.

        :return: The medialive_cdn of this CesQueryRespQuery.
        :rtype: :class:`huaweicloudsdklive.v1.CesDimsItem`
        """
        return self._medialive_cdn

    @medialive_cdn.setter
    def medialive_cdn(self, medialive_cdn):
        r"""Sets the medialive_cdn of this CesQueryRespQuery.

        :param medialive_cdn: The medialive_cdn of this CesQueryRespQuery.
        :type medialive_cdn: :class:`huaweicloudsdklive.v1.CesDimsItem`
        """
        self._medialive_cdn = medialive_cdn

    @property
    def medialive_package(self):
        r"""Gets the medialive_package of this CesQueryRespQuery.

        :return: The medialive_package of this CesQueryRespQuery.
        :rtype: :class:`huaweicloudsdklive.v1.CesDimsItem`
        """
        return self._medialive_package

    @medialive_package.setter
    def medialive_package(self, medialive_package):
        r"""Sets the medialive_package of this CesQueryRespQuery.

        :param medialive_package: The medialive_package of this CesQueryRespQuery.
        :type medialive_package: :class:`huaweicloudsdklive.v1.CesDimsItem`
        """
        self._medialive_package = medialive_package

    @property
    def medialive_connect(self):
        r"""Gets the medialive_connect of this CesQueryRespQuery.

        :return: The medialive_connect of this CesQueryRespQuery.
        :rtype: :class:`huaweicloudsdklive.v1.CesDimsItem`
        """
        return self._medialive_connect

    @medialive_connect.setter
    def medialive_connect(self, medialive_connect):
        r"""Sets the medialive_connect of this CesQueryRespQuery.

        :param medialive_connect: The medialive_connect of this CesQueryRespQuery.
        :type medialive_connect: :class:`huaweicloudsdklive.v1.CesDimsItem`
        """
        self._medialive_connect = medialive_connect

    @property
    def medialive_tailor(self):
        r"""Gets the medialive_tailor of this CesQueryRespQuery.

        :return: The medialive_tailor of this CesQueryRespQuery.
        :rtype: :class:`huaweicloudsdklive.v1.CesDimsItem`
        """
        return self._medialive_tailor

    @medialive_tailor.setter
    def medialive_tailor(self, medialive_tailor):
        r"""Sets the medialive_tailor of this CesQueryRespQuery.

        :param medialive_tailor: The medialive_tailor of this CesQueryRespQuery.
        :type medialive_tailor: :class:`huaweicloudsdklive.v1.CesDimsItem`
        """
        self._medialive_tailor = medialive_tailor

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
        if not isinstance(other, CesQueryRespQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
